#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Programa els posts de posts.json al canal d'Instagram de Buffer (API GraphQL).

Ús:
  BUFFER_API_KEY=... python3 publish_buffer.py            # dry-run: introspecciona, llista i imprimeix les mutacions
  BUFFER_API_KEY=... python3 publish_buffer.py --send     # crea els posts programats
  BUFFER_API_KEY=... python3 publish_buffer.py --status   # només llista el que hi ha programat al canal

L'script s'adapta a l'esquema real (introspecció) perquè l'API és beta i els noms poden canviar.
"""
import os, sys, json, time
import httpx

API = "https://api.buffer.com"
KEY = os.environ.get("BUFFER_API_KEY")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_FILE = os.path.join(ROOT, "posts.json")
STATE_FILE = os.path.join(ROOT, "buffer_state.json")

def gql(query, variables=None):
    r = httpx.post(API, json={"query": query, "variables": variables or {}},
                   headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}, timeout=60)
    r.raise_for_status()
    j = r.json()
    if "errors" in j:
        raise RuntimeError(json.dumps(j["errors"], ensure_ascii=False, indent=1))
    return j["data"]

def type_fields(name):
    d = gql("""query($n:String!){ __type(name:$n){ name kind inputFields{ name type{ name kind ofType{ name kind ofType{ name kind ofType{ name kind }}}}} fields{ name args{ name } type{ name kind ofType{ name kind ofType{ name kind }}}} enumValues{ name } } }""", {"n": name})
    return d["__type"]

def tname(t):
    while t and not t.get("name"):
        t = t.get("ofType")
    return t.get("name") if t else None

def introspect():
    info = {}
    for n in ["CreatePostInput", "Mutation", "Query", "PostSchedulingType", "PostMode", "CreatePostAssetsInput",
              "AssetsInput", "PostMetadataInput", "InstagramPostMetadataInput", "InstagramMetadataInput", "InstagramPostType"]:
        try:
            t = type_fields(n)
            if t: info[n] = t
        except Exception as e:
            pass
    return info

def find_org_and_channel():
    # Provem les formes més habituals de l'esquema
    for q in ["query{ account{ organizations{ id name channels{ id name service displayName } } } }",
              "query{ organizations{ id name channels{ id name service displayName } } }",
              "query{ me{ organizations{ id name channels{ id name service } } } }"]:
        try:
            d = gql(q)
            orgs = d.get("account", d).get("organizations") if isinstance(d.get("account", d), dict) else d.get("organizations")
            if orgs: return orgs
        except Exception as e:
            last = e
    raise RuntimeError(f"No he pogut llistar organitzacions/canals: {last}")

def list_posts(channel_id):
    # Llista posts del canal (scheduled). L'esquema real pot variar: provem dues formes.
    for q in ["""query($c:ID!){ posts(input:{filters:{channelIds:[$c]}, first:200}){ edges{ node{ id text dueAt status assets{ id } } } } }""",
              """query($c:ID!){ posts(channelIds:[$c], first:200){ edges{ node{ id text dueAt status } } } }"""]:
        try:
            d = gql(q, {"c": channel_id})
            return [e["node"] for e in d["posts"]["edges"]]
        except Exception as e:
            last = e
    print("  (no he pogut llistar els posts existents:", str(last)[:200], ")")
    return []

def build_input(fields, channel_id, p):
    names = {f["name"]: tname(f["type"]) for f in fields}
    inp = {"text": p["caption"], "schedulingType": "automatic", "mode": "customScheduled", "dueAt": p["due_at"]}
    if "channelId" in names: inp["channelId"] = channel_id
    elif "channelIds" in names: inp["channelIds"] = [channel_id]
    # imatges
    if "assets" in names:
        at = names["assets"]
        afields = {f["name"] for f in (type_fields(at) or {}).get("inputFields", [])} if at else set()
        if "images" in afields:
            inp["assets"] = {"images": [{"url": u} for u in p["images"]]}
        else:
            inp["assets"] = [{"url": u} for u in p["images"]]
    # metadata instagram: tipus post + primer comentari amb hashtags
    first_comment_done = False
    if "metadata" in names:
        mt = names["metadata"]; mfields = {f["name"]: tname(f["type"]) for f in (type_fields(mt) or {}).get("inputFields", [])}
        if "instagram" in mfields:
            it = mfields["instagram"]; ifields = {f["name"] for f in (type_fields(it) or {}).get("inputFields", [])}
            ig = {}
            if "type" in ifields: ig["type"] = "post"
            if "shouldShareToFeed" in ifields: ig["shouldShareToFeed"] = True
            for fc in ("firstComment", "first_comment"):
                if fc in ifields: ig[fc] = p["hashtags"]; first_comment_done = True
            inp["metadata"] = {"instagram": ig}
    if not first_comment_done:
        inp["text"] = p["caption"] + "\n\n" + p["hashtags"]
    return inp

MUT = """mutation($input: CreatePostInput!){ createPost(input:$input){ ... on PostActionSuccess { post { id dueAt status } } ... on MutationError { message } } }"""

def main():
    if not KEY:
        sys.exit("Falta BUFFER_API_KEY a l'entorn.")
    send = "--send" in sys.argv; status = "--status" in sys.argv
    posts = json.load(open(POSTS_FILE, encoding="utf-8"))
    state = json.load(open(STATE_FILE)) if os.path.exists(STATE_FILE) else {}

    orgs = find_org_and_channel()
    ig = [c for o in orgs for c in o.get("channels", []) if (c.get("service") or "").lower() == "instagram"]
    if not ig: sys.exit(f"No hi ha cap canal d'Instagram. Canals: {json.dumps(orgs, indent=1)}")
    ch = ig[0]; print("Canal Instagram:", ch)

    existing = list_posts(ch["id"])
    print(f"Posts existents al canal: {len(existing)}")
    by_day = {}
    for e in existing:
        if e.get("dueAt"): by_day.setdefault(e["dueAt"][:10], []).append(e)
    if status:
        for d in sorted(by_day): print(d, [ (e['status'], (e.get('text') or '')[:40]) for e in by_day[d]])
        return

    info = introspect()
    cp = info.get("CreatePostInput")
    if not cp: sys.exit("No trobo CreatePostInput a l'esquema; revisa l'API.")
    fields = cp["inputFields"]
    print("CreatePostInput:", [f["name"] for f in fields])

    for p in posts:
        if p["id"] in state:
            print(p["id"], "ja creat:", state[p["id"]]); continue
        day = p["due_at"][:10]
        dup = [e for e in by_day.get(day, []) if "marca pròpia" in (e.get("text") or "").lower() or p["title"].lower() in (e.get("text") or "").lower()]
        if dup:
            print(p["id"], "DUPLICAT el", day, "→ salto"); continue
        inp = build_input(fields, ch["id"], p)
        if not send:
            print(f"\n--- DRY RUN {p['id']} {p['due_local']} ({len(p['images'])} imatges)")
            print(json.dumps({k: (v if k != "text" else v[:120] + "…") for k, v in inp.items()}, ensure_ascii=False, indent=1))
            continue
        d = gql(MUT, {"input": inp})
        res = d["createPost"]
        if res.get("post"):
            state[p["id"]] = res["post"]; print(p["id"], "OK", res["post"])
        else:
            print(p["id"], "ERROR", res);
        json.dump(state, open(STATE_FILE, "w"), indent=1)
        time.sleep(1.5)

if __name__ == "__main__":
    main()
