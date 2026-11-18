#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Programa els posts de posts.json al canal d'Instagram de Buffer (API GraphQL).

Ús:
  python publish_buffer.py --status                      # què hi ha a la cua del canal i límits del pla
  python publish_buffer.py                               # dry-run: imprimeix les mutacions, no envia res
  python publish_buffer.py --send                        # pla de pagament: programa tots els pendents
  python publish_buffer.py --send --max-queue 10 --max-own 5
        # pla Free: la cua del compte és de 10 peces (posts I stories de qualsevol origen).
        # --max-queue: no passar mai de N peces a la cua; --max-own: com a màxim N posts d'aquesta
        # sèrie alhora, perquè el pipeline diari (5 peces cada vespre) hi càpiga sempre.

BUFFER_API_KEY: de l'entorn o, si no hi és, del .env del pipeline (C:\\FarmaServer\\xxss-farmacia\\.env).

Idempotent: buffer_state.json (local, no versionat) recorda quins posts s'han creat; a més es compara
l'inici de la caption amb el que hi ha programat o enviat al canal. Si la data d'un post ja ha passat,
es mou al següent dia lliure d'aquesta sèrie a la mateixa hora. hold.txt llista ids que NO s'envien.

Esquema verificat per introspecció (2026-11-07 i 2026-11-18):
  channels(input:{organizationId}) · posts(input:{organizationId, filter:{channelIds,status}}, first)
  createPost(input:{channelId, text, assets:[{image:{url, metadata:{altText}}}], dueAt, mode,
                    schedulingType, needsApproval!, metadata:{instagram:{type, shouldShareToFeed!}}})
  El primer comentari (firstComment) és de pagament: al pla Free els hashtags van al final del text.
"""
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone

import httpx

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

API = "https://api.buffer.com"
HERE = os.path.dirname(os.path.abspath(__file__))
POSTS_FILE = os.path.join(HERE, "posts.json")
STATE_FILE = os.path.join(HERE, "buffer_state.json")
HOLD_FILE = os.path.join(HERE, "hold.txt")
PIPELINE_ENV = os.environ.get("XXSS_ENV_FILE") or os.path.normpath(os.path.join(HERE, "..", "..", "..", "xxss-farmacia", ".env"))
MAX_CAPTION = 2200


def env_value(name):
    v = os.environ.get(name)
    if v:
        return v.strip()
    if os.path.exists(PIPELINE_ENV):
        for line in open(PIPELINE_ENV, encoding="utf-8", errors="replace"):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip()
    return None


KEY = env_value("BUFFER_API_KEY")
FIRST_COMMENT = (env_value("BUFFER_FIRST_COMMENT") or "0") == "1"   # només amb pla de pagament


def gql(query, variables=None, tries=4):
    for attempt in range(tries):
        r = httpx.post(API, json={"query": query, "variables": variables or {}},
                       headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}, timeout=60)
        if r.status_code == 429:
            wait = int(r.headers.get("Retry-After") or 0) or 60 * (attempt + 1)
            print(f"  429 (límit de l'API): espero {wait} s")
            time.sleep(min(wait, 900))
            continue
        r.raise_for_status()
        j = r.json()
        if j.get("errors"):
            raise RuntimeError(json.dumps(j["errors"], ensure_ascii=False, indent=1))
        return j["data"]
    raise RuntimeError("l'API de Buffer segueix tornant 429 després de diversos intents")


def org_and_channel():
    acc = gql("{ account { organizations { id name limits { scheduledPosts channels } } } }")["account"]
    org = acc["organizations"][0]
    chans = gql("query($i: ChannelsInput!){ channels(input:$i){ id name service type isDisconnected } }",
                {"i": {"organizationId": org["id"]}})["channels"]
    fixed = env_value("BUFFER_INSTAGRAM_CHANNEL_ID")
    ig = [c for c in chans if c["service"].lower() == "instagram" and (not fixed or c["id"] == fixed)]
    if not ig:
        sys.exit(f"No hi ha cap canal d'Instagram connectat. Canals: {chans}")
    return org, ig[0]


def list_posts(org_id, channel_id, status):
    q = """query($i: PostsInput!, $n: Int){ posts(input:$i, first:$n){ edges{ node{ id text dueAt status
            metadata{ ... on InstagramPostMetadata { type } } } } } }"""
    d = gql(q, {"i": {"organizationId": org_id, "filter": {"channelIds": [channel_id], "status": [status]}}, "n": 100})
    return [e["node"] for e in d["posts"]["edges"]]


def caption_head(text):
    return " ".join((text or "").split())[:60].lower()


def build_input(channel_id, p):
    text = p["caption"].rstrip()
    ig = {"type": "post", "shouldShareToFeed": True}
    if p.get("hashtags"):
        if FIRST_COMMENT:
            ig["firstComment"] = p["hashtags"]
        else:
            text = f"{text}\n\n{p['hashtags']}"
    if len(text) > MAX_CAPTION:
        raise ValueError(f"{p['id']}: caption + hashtags fan {len(text)} caràcters (màxim {MAX_CAPTION})")
    n = len(p["images"])
    return {
        "channelId": channel_id,
        "text": text,
        "assets": [{"image": {"url": u, "metadata": {"altText": f"{p['title']} ({i + 1}/{n})"}}} for i, u in enumerate(p["images"])],
        "dueAt": p["due_at"],
        "mode": "customScheduled",
        "schedulingType": "automatic",
        "needsApproval": False,
        "source": "xxss-marca-propia",
        "metadata": {"instagram": ig},
    }


MUT = """mutation($input: CreatePostInput!){ createPost(input:$input){ __typename
  ... on PostActionSuccess { post { id dueAt status } } ... on MutationError { message } } }"""


def images_served(urls):
    bad = []
    with httpx.Client(timeout=20, follow_redirects=True) as c:
        for u in urls:
            try:
                r = c.head(u)
                if r.status_code != 200 or "image" not in r.headers.get("content-type", ""):
                    bad.append(u)
            except httpx.HTTPError:
                bad.append(u)
    return bad


def arg_int(flag, default):
    return int(sys.argv[sys.argv.index(flag) + 1]) if flag in sys.argv else default


def read_hold():
    held = {}
    if os.path.exists(HOLD_FILE):
        for line in open(HOLD_FILE, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                pid, _, why = line.partition(" ")
                held[pid] = why.strip()
    return held


def main():
    if not KEY:
        sys.exit("Falta BUFFER_API_KEY (entorn o .env del pipeline).")
    send = "--send" in sys.argv
    status = "--status" in sys.argv
    max_queue = arg_int("--max-queue", 0)   # 0 = sense límit (plans de pagament)
    max_own = arg_int("--max-own", 0)       # 0 = sense límit propi
    now = datetime.now(timezone.utc)
    posts = sorted(json.load(open(POSTS_FILE, encoding="utf-8")), key=lambda x: x["due_at"])
    state = json.load(open(STATE_FILE, encoding="utf-8")) if os.path.exists(STATE_FILE) else {}
    held = read_hold()

    org, ch = org_and_channel()
    print(f"Canal: {ch['service']} {ch['name']} ({ch['id']}) · pla: màxim {org['limits']['scheduledPosts']} peces a la cua")
    scheduled = list_posts(org["id"], ch["id"], "scheduled")
    sent = list_posts(org["id"], ch["id"], "sent")
    heads = {caption_head(e.get("text")) for e in scheduled + sent}
    own_heads = {caption_head(p["caption"]): p["id"] for p in posts}
    own_scheduled = [e for e in scheduled if caption_head(e.get("text")) in own_heads]
    print(f"A la cua ara: {len(scheduled)} ({len(own_scheduled)} de marca pròpia) · enviats (últims 100): {len(sent)}")

    if status:
        for e in sorted(scheduled, key=lambda x: x.get("dueAt") or ""):
            kind = (e.get("metadata") or {}).get("type") or "?"
            mine = own_heads.get(caption_head(e.get("text")), "")
            print(f"  {e.get('dueAt')}  {kind:<6} {mine:<4} {' '.join((e.get('text') or '').split())[:70]}")
        done = [p["id"] for p in posts if p["id"] in state or caption_head(p["caption"]) in heads]
        print(f"Marca pròpia: {len(done)} creats de {len(posts)} · retinguts (hold.txt): {len(held)}")
        return

    free_queue = (max_queue - len(scheduled)) if max_queue else 10 ** 6
    free_own = (max_own - len(own_scheduled)) if max_own else 10 ** 6
    free = min(free_queue, free_own)
    print(f"Forats: cua {free_queue if max_queue else '∞'} · propis {free_own if max_own else '∞'} → es poden crear {max(free, 0) if free < 10 ** 6 else 'tots'}")
    used_days = {(e.get("dueAt") or "")[:10] for e in own_scheduled}
    created = pending = 0
    for p in posts:
        pid = p["id"]
        if pid in state or caption_head(p["caption"]) in heads:
            continue
        if pid in held:
            print(f"{pid} retingut: {held[pid]}")
            continue
        if free <= 0:
            pending += 1
            continue
        due = datetime.strptime(p["due_at"], "%Y-%m-%dT%H:%M:%S.000Z").replace(tzinfo=timezone.utc)
        while due <= now + timedelta(hours=1) or (due.strftime("%Y-%m-%d") in used_days and due.strftime("%Y-%m-%d") != p["due_at"][:10]):
            due += timedelta(days=1)
        new_due = due.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        if new_due != p["due_at"]:
            print(f"{pid} reprogramat de {p['due_at']} a {new_due}")
            p = dict(p, due_at=new_due)
        inp = build_input(ch["id"], p)
        if not send:
            print(f"\n--- DRY RUN {pid} {p['due_at']} ({len(p['images'])} imatges) {p['title']}")
            print(json.dumps({k: (v if k != "text" else v[:110] + "…") for k, v in inp.items()}, ensure_ascii=False, indent=1))
            free -= 1
            used_days.add(new_due[:10])
            continue
        bad = images_served(p["images"])
        if bad:
            print(f"{pid} NO creat: imatges no servides per GitHub Pages: {bad[:2]}")
            continue
        res = gql(MUT, {"input": inp})["createPost"]
        if res.get("post"):
            state[pid] = {**res["post"], "title": p["title"]}
            json.dump(state, open(STATE_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"{pid} OK {res['post']['dueAt']} {p['title']}")
            created += 1
            free -= 1
            used_days.add(new_due[:10])
        else:
            print(f"{pid} ERROR {res.get('message') or res}")
            if "limit" in str(res.get("message", "")).lower():
                break
        time.sleep(2)
    print(f"\nCreats ara: {created} · pendents per a properes execucions: {pending} · retinguts: {len(held)}")


if __name__ == "__main__":
    main()
