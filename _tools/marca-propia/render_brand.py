# -*- coding: utf-8 -*-
"""Renderitza la sèrie «La nostra marca» (producte heroi, 4 slides) amb la plantilla del compte."""
import sys, json, html, base64
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from content_brand import BRAND_POSTS
from content import BASE_TAGS

ROOT = Path(__file__).resolve().parents[1]
CUT = ROOT / "cut"; OUT = ROOT / "out"; LOGO = ROOT / "brand" / "logo_crop.png"
W, H = 1080, 1350

def data_uri(path):
    return "data:image/png;base64," + base64.b64encode(Path(path).read_bytes()).decode()
LOGO_URI = data_uri(LOGO)

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { width: 1080px; height: 1350px; background: #F4F8F7; overflow: hidden; }
body { font-family: 'Open Sans', sans-serif; color: #1C2B2B; position: relative; }
.logo { position: absolute; left: 60px; top: 50px; width: 660px; height: 100px; }
.label { position: absolute; right: 72px; top: 86px; font-weight: 700; font-size: 24px; letter-spacing: 2px; color: #065F65; }
.rule { position: absolute; left: 72px; top: 1224px; width: 936px; height: 3px; background: #83C35F; }
.handle { position: absolute; left: 72px; top: 1258px; font-weight: 600; font-size: 28px; color: #5B6E6E; }
.pill { position: absolute; right: 72px; top: 1250px; background: #065F65; color: #fff; font-weight: 700; font-size: 28px; line-height: 50px; padding: 0 26px; border-radius: 999px; }
/* portada */
.headline { position: absolute; left: 72px; top: 176px; width: 936px; max-height: 164px; overflow: hidden; font-weight: 700; font-size: 70px; line-height: 82px; color: #004349; letter-spacing: -0.5px; }
.headline.small { font-size: 60px; line-height: 72px; }
.headline.xsmall { font-size: 52px; line-height: 62px; }
.hero { position: absolute; left: 72px; top: 372px; width: 936px; height: 500px; background: #fff; border: 3px solid #065F65; border-radius: 28px; overflow: hidden; display: flex; align-items: center; justify-content: center; padding: 24px; }
.hero img { max-width: 100%; max-height: 100%; object-fit: contain; }
.badge { position: absolute; right: 44px; top: 336px; width: 196px; height: 196px; border-radius: 50%; background: #004349; color: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; box-shadow: 0 6px 18px rgba(0,67,73,.25); padding: 10px; }
.badge .b1 { font-weight: 600; font-size: 20px; letter-spacing: 1px; line-height: 24px; }
.badge .b2 { font-weight: 800; font-size: 40px; line-height: 44px; color: #B8E986; }
.badge .b2.long { font-size: 28px; line-height: 32px; }
.args { position: absolute; left: 72px; top: 904px; width: 936px; max-height: 300px; overflow: hidden; }
.arg { display: flex; gap: 18px; align-items: flex-start; margin-bottom: 14px; font-weight: 600; font-size: 34px; line-height: 46px; color: #1C2B2B; }
.chk { flex: 0 0 38px; width: 38px; height: 38px; margin-top: 4px; border-radius: 50%; background: #83C35F; color: #fff; font-weight: 800; font-size: 26px; line-height: 38px; text-align: center; }
/* slides partits */
.kicker { position: absolute; left: 72px; top: 180px; font-weight: 700; font-size: 26px; letter-spacing: 3px; color: #065F65; }
.stitle { position: absolute; left: 72px; top: 216px; width: 936px; max-height: 70px; overflow: hidden; font-weight: 700; font-size: 54px; line-height: 66px; color: #004349; }
.side { position: absolute; left: 72px; top: 318px; width: 400px; height: 560px; background: #fff; border: 3px solid #065F65; border-radius: 28px; overflow: hidden; display: flex; align-items: center; justify-content: center; padding: 20px; }
.side img { max-width: 100%; max-height: 100%; object-fit: contain; }
.col { position: absolute; left: 512px; top: 318px; width: 496px; max-height: 880px; overflow: hidden; }
.item { margin-bottom: 26px; }
.item .n { font-weight: 700; font-size: 34px; line-height: 42px; color: #004349; }
.item .d { font-weight: 400; font-size: 30px; line-height: 40px; color: #1C2B2B; margin-top: 4px; }
.cta { position: absolute; left: 72px; top: 1118px; background: #004349; color: #fff; font-weight: 700; font-size: 34px; line-height: 70px; padding: 0 40px; border-radius: 999px; }
.prod { position: absolute; left: 72px; top: 1000px; width: 400px; font-weight: 600; font-size: 24px; line-height: 32px; color: #5B6E6E; text-align: center; }
"""

def shell(inner, idx, total):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<img class="logo" src="{LOGO_URI}"><div class="label">LA NOSTRA MARCA</div>
{inner}
<div class="rule"></div><div class="handle">@farmaciadeldiamant</div><div class="pill">{idx}/{total}</div></body></html>"""

def cover(p, img, small=0):
    b1, b2 = p["badge"]; long = len(b2) > 7
    args = "".join(f'<div class="arg"><div class="chk">✓</div><div>{html.escape(a)}</div></div>' for a in p["args"])
    return shell(f"""
<div class="headline{' small' if small==1 else (' xsmall' if small>=2 else '')}" id="title">{html.escape(p["headline"])}</div>
<div class="hero"><img src="{data_uri(img)}"></div>
<div class="badge"><div class="b1">{html.escape(b1)}</div><div class="b2{' long' if long else ''}">{html.escape(b2)}</div></div>
<div class="args" id="body">{args}</div>""", 1, 4)

def split(p, img, kicker, title, items, idx, cta=None):
    its = "".join(f'<div class="item"><div class="n">{html.escape(n)}</div><div class="d">{html.escape(d)}</div></div>' for n, d in items)
    extra = f'<div class="cta">{html.escape(cta)}</div>' if cta else ""
    return shell(f"""
<div class="kicker">{html.escape(kicker)}</div>
<div class="stitle" id="title">{html.escape(title)}</div>
<div class="side"><img src="{data_uri(img)}"></div>
<div class="col" id="body">{its}</div>{extra}""", idx, 4)

def main(only=None):
    from playwright.sync_api import sync_playwright
    report = {}
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", args=["--no-sandbox"])
        pg = browser.new_context(viewport={"width": W, "height": H}, device_scale_factor=1).new_page()
        for p in BRAND_POSTS:
            if only and p["id"] not in only: continue
            d = OUT / f"{p['date']}-{p['slug']}"; d.mkdir(parents=True, exist_ok=True)
            img = CUT / f"{p['code']}.png"
            pages = [
                ("cover", None),
                ("split", ("QUÈ PORTA", p["name"], p["porta"], 2, None)),
                ("split", ("PER QUÈ LA NOSTRA MARCA", p["name"], p["perque"], 3, None)),
                ("split", ("EL NOSTRE CONSELL", p["name"], p["consell"], 4, "Demana'l al taulell →")),
            ]
            rep = []
            for k, (kind, spec) in enumerate(pages, start=1):
                for attempt in range(3):
                    h = cover(p, img, small=attempt) if kind == "cover" else split(p, img, *spec)
                    pg.set_content(h, wait_until="load"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(50)
                    ov = pg.evaluate("""() => { const t=document.getElementById('title'), b=document.getElementById('body');
                        return {title:[t.scrollHeight,t.clientHeight], body:[b.scrollHeight,b.clientHeight]}; }""")
                    ok = ov["title"][0] <= ov["title"][1] + 8 and ov["body"][0] <= ov["body"][1] + 2
                    if ok or kind != "cover": break
                pg.screenshot(path=str(d / f"slide-{k:02d}.png"))
                rep.append(dict(slide=k, overflow=ov, ok=ok))
            (d / "caption.txt").write_text(p["caption"], encoding="utf-8")
            (d / "hashtags.txt").write_text(" ".join(BASE_TAGS + p["tags"]), encoding="utf-8")
            report[p["id"]] = rep
            print(p["id"], d.name, "OVERFLOW!" if any(not r["ok"] for r in rep) else "ok")
        browser.close()
    (OUT / "render-brand-report.json").write_text(json.dumps(report, indent=1))

if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
