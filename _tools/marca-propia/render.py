# -*- coding: utf-8 -*-
"""Renderitza els slides 1080x1350 dels posts de marca pròpia amb la plantilla de @farmaciadeldiamant."""
import os, sys, json, html, base64
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from content import POSTS

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "cut"
OUT = ROOT / "out"
BRAND = ROOT / "brand"
LOGO = BRAND / "logo_crop.png"
W, H = 1080, 1350

# --- logo: retall exacte del slide existent (mateix fons, mateixa posició) ---
if not LOGO.exists():
    im = Image.open("/home/claude/xxss-media/2026-11-26-dormir/slide-01.png").convert("RGB")
    im.crop((60, 50, 720, 150)).save(LOGO)

def data_uri(path):
    b = Path(path).read_bytes()
    ext = Path(path).suffix.lower().lstrip(".")
    mime = "image/png" if ext == "png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(b).decode()

LOGO_URI = data_uri(LOGO)

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { width: 1080px; height: 1350px; background: #F4F8F7; overflow: hidden; }
body { font-family: 'Open Sans', sans-serif; color: #1C2B2B; position: relative; }
.logo { position: absolute; left: 60px; top: 50px; width: 660px; height: 100px; }
.label { position: absolute; right: 72px; top: 84px; font-weight: 600; font-size: 26px; color: #065F65; }
.title { position: absolute; left: 72px; top: 178px; width: 936px; max-height: 160px; overflow: hidden;
         font-weight: 700; font-size: 66px; line-height: 78px; color: #004349; letter-spacing: -0.5px; }
.title.small { font-size: 58px; line-height: 70px; }
.frame { position: absolute; left: 72px; top: 380px; width: 936px; height: 600px; background: #FFFFFF;
         border: 3px solid #065F65; border-radius: 28px; overflow: hidden;
         display: flex; align-items: center; justify-content: center; gap: 18px; padding: 26px; }
.frame img { max-height: 100%; max-width: 100%; object-fit: contain; }
.frame.multi { display: grid; grid-template-columns: minmax(0,1fr) minmax(0,1fr); grid-template-rows: minmax(0,1fr) minmax(0,1fr); gap: 14px; padding: 22px; }
.frame.multi img { width: 100%; height: 100%; min-width: 0; min-height: 0; object-fit: contain; }
.frame.multi.three { grid-template-columns: minmax(0,1fr) minmax(0,1fr) minmax(0,1fr); grid-template-rows: minmax(0,1fr); }
.frame.tall { top: 290px; height: 690px; }
.body { position: absolute; left: 72px; top: 1008px; width: 936px; max-height: 206px; overflow: hidden;
        font-weight: 400; font-size: 40px; line-height: 56px; color: #1C2B2B; }
.body.small { font-size: 36px; line-height: 50px; }
.kind { display: block; width: fit-content; font-weight: 600; font-size: 26px; line-height: 36px; color: #065F65;
        border: 2px solid #065F65; border-radius: 999px; padding: 0 16px; margin-bottom: 8px; }
.rule { position: absolute; left: 72px; top: 1224px; width: 936px; height: 3px; background: #83C35F; }
.handle { position: absolute; left: 72px; top: 1258px; font-weight: 600; font-size: 28px; color: #5B6E6E; }
.pill { position: absolute; right: 72px; top: 1250px; background: #065F65; color: #fff; font-weight: 700;
        font-size: 28px; line-height: 50px; padding: 0 26px; border-radius: 999px; }
.swipe { color: #065F65; font-weight: 600; }
"""

KIND_LABEL = {"SUP": "Complement alimentari", "PS": "Producte sanitari", "COS": "Cosmètic"}

def page(title, body_html, images, idx, total, label="Marca pròpia", multi=False, small_title=False, small_body=False, tall=False):
    imgs = "".join(f'<img src="{data_uri(p)}">' for p in images)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<img class="logo" src="{LOGO_URI}">
<div class="label">{html.escape(label)}</div>
<div class="title{' small' if small_title else ''}" id="title">{html.escape(title)}</div>
<div class="frame{' multi' if multi else ''}{' three' if multi and len(images)==3 else ''}{' tall' if tall else ''}">{imgs}</div>
<div class="body{' small' if small_body else ''}" id="body">{body_html}</div>
<div class="rule"></div>
<div class="handle">@farmaciadeldiamant</div>
<div class="pill">{idx}/{total}</div>
</body></html>"""

def build_pages(post):
    n = len(post["products"]) + 1
    pages = []
    # portada
    hook = html.escape(post["hook"]) + ' <span class="swipe">Llisca per veure\'ls →</span>'
    pages.append(dict(title=post["title"], body=hook, images=[SRC / f"{p['code']}.png" for p in post["products"]],
                      idx=1, total=n, multi=True))
    for i, p in enumerate(post["products"], start=2):
        body = f'<span class="kind">{KIND_LABEL[p["kind"]]}</span>{html.escape(p["body"])}'
        pages.append(dict(title=p["name"], body=body, images=[SRC / f"{p['code']}.png"], idx=i, total=n, multi=False))
    return pages

def main(only=None):
    from playwright.sync_api import sync_playwright
    report = {}
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", args=["--no-sandbox"])
        ctx = browser.new_context(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg = ctx.new_page()
        for post in POSTS:
            if only and post["id"] not in only: continue
            d = OUT / f"{post['date']}-{post['slug']}"
            d.mkdir(parents=True, exist_ok=True)
            rep = []
            for k, spec in enumerate(build_pages(post), start=1):
                tall = False
                for attempt in range(3):
                    sb = attempt >= 1; st = attempt >= 2
                    pg.set_content(page(spec["title"], spec["body"], spec["images"], spec["idx"], spec["total"],
                                        multi=spec["multi"], small_title=st, small_body=sb, tall=tall), wait_until="load")
                    pg.evaluate("document.fonts.ready")
                    pg.wait_for_timeout(60)
                    if not tall and attempt == 0 and pg.evaluate("document.getElementById('title').scrollHeight") < 120:
                        tall = True
                        pg.set_content(page(spec["title"], spec["body"], spec["images"], spec["idx"], spec["total"],
                                            multi=spec["multi"], small_title=st, small_body=sb, tall=tall), wait_until="load")
                        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(60)
                    ov = pg.evaluate("""() => {
                        const t=document.getElementById('title'), b=document.getElementById('body');
                        return {title:[t.scrollHeight,t.clientHeight], body:[b.scrollHeight,b.clientHeight]};}""")
                    ok = ov["title"][0] <= ov["title"][1] + 8 and ov["body"][0] <= ov["body"][1] + 2
                    if ok: break
                out = d / f"slide-{k:02d}.png"
                pg.screenshot(path=str(out), full_page=False)
                rep.append(dict(slide=k, overflow=ov, ok=ok, attempt=attempt, tall=tall))
            # caption i hashtags
            (d / "caption.txt").write_text(post["caption"], encoding="utf-8")
            from content import BASE_TAGS
            (d / "hashtags.txt").write_text(" ".join(BASE_TAGS + post["tags"]), encoding="utf-8")
            report[post["id"]] = rep
            bad = [r for r in rep if not r["ok"]]
            print(post["id"], d.name, f"{len(rep)} slides", "OVERFLOW!" if bad else "ok")
        browser.close()
    (OUT / "render-report.json").write_text(json.dumps(report, indent=1))

if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
