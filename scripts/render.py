import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from posts import POSTS, A
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).resolve().parent.parent / "posts" / "2026-11" / "lote-1"
OUT.mkdir(exist_ok=True)

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
.slide{position:relative;width:1080px;height:1350px;padding:84px 88px 80px;display:flex;flex-direction:column;overflow:hidden;font-family:'Inter',sans-serif}
.top,.bottom{position:relative;z-index:3;display:flex;justify-content:space-between;align-items:center}
.top{height:60px}
.bottom{height:48px;font:500 24px 'Inter';letter-spacing:.02em}
.content{position:relative;z-index:2;flex:1;display:flex;flex-direction:column;justify-content:center}
.content.cover{justify-content:flex-start;padding-top:100px}
.fade{position:absolute;left:0;right:0;bottom:0;height:330px;z-index:2;background:linear-gradient(to bottom,rgba(14,13,18,0),#0E0D12 70%)}
.row h2{font-size:64px}
.cover .lead{max-width:620px}
.count{font:500 24px 'Inter';letter-spacing:.08em}
.mt24{margin-top:24px}.mt32{margin-top:32px}.mt40{margin-top:40px}.mt48{margin-top:48px}.mt56{margin-top:56px}
.lead{font:400 38px/1.45 'Inter'}
.list .item p.big,.big{font:500 40px/1.35 'Inter';margin-top:0}
.list .item{display:flex;gap:28px;padding:28px 0}
.list .item h3{font-size:40px;line-height:1.2}
.list .item p{font:400 31px/1.4 'Inter';margin-top:6px}
.card{border-radius:28px;padding:40px 44px}
.card h3{font-size:40px;line-height:1.2;margin-top:14px}
.card p{font:400 30px/1.4 'Inter';margin-top:12px}
.card-tag{font:600 22px 'Inter';letter-spacing:.16em;text-transform:uppercase}
.two{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.two .card h3{font-size:36px}
.cta{display:flex;flex-direction:column;align-items:flex-start;gap:18px}
.btn{display:inline-flex;padding:26px 42px;border-radius:999px;font:600 32px 'Inter'}
.cta-sub{font:500 26px 'Inter'}
.row{display:flex;gap:56px;align-items:center}
.col-text{flex:1}
.phone{flex:0 0 400px;height:830px;border-radius:52px;padding:12px;overflow:hidden}
.phone img{width:100%;height:100%;object-fit:cover;object-position:top;border-radius:42px;display:block}
.note{position:absolute;left:0;bottom:-6px;font:400 22px 'Inter';z-index:3}
.shot{display:block;border-radius:22px}
.shot-wide{width:904px}
.shot-crop{width:904px}
.shot-cover{position:absolute;left:0;top:520px;width:1240px;z-index:1}
.steps{display:flex;flex-direction:column;gap:18px}
.step{display:flex;align-items:center;gap:24px;font:500 36px 'Inter';padding:22px 28px;border-radius:20px}
.step span{display:inline-flex;width:56px;height:56px;border-radius:50%;align-items:center;justify-content:center;font:600 26px 'Inter'}
.swipe{display:flex;align-items:center;gap:12px}

.wm-u{position:absolute;right:-60px;bottom:-260px;font:400 1100px/1 'Gelasio';color:rgba(200,152,46,.055);z-index:1;pointer-events:none}
.wm-v{position:absolute;right:-90px;bottom:-40px;width:640px;opacity:.10;z-index:1}
/* ---------- VORINN ---------- */
.v{background:#030814;color:#CBD5E1}
.v .bg{position:absolute;inset:0;z-index:0;
  background:
   radial-gradient(circle at 88% 6%, rgba(47,149,255,.30), transparent 42%),
   radial-gradient(circle at 0% 100%, rgba(47,149,255,.14), transparent 45%)}
.v .grid{position:absolute;inset:0;z-index:0;
  background-image:linear-gradient(rgba(148,163,184,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(148,163,184,.07) 1px,transparent 1px);
  background-size:72px 72px;
  -webkit-mask-image:radial-gradient(ellipse at 75% 15%,#000 0%,transparent 65%)}
.v h1{font-family:'Inter Display';font-weight:600;font-size:94px;line-height:1.04;letter-spacing:-.025em;color:#fff}
.v h2{font-family:'Inter Display';font-weight:600;font-size:72px;line-height:1.08;letter-spacing:-.02em;color:#fff}
.v h3{font-family:'Inter Display';font-weight:600;color:#fff}
.v .acc{background:linear-gradient(90deg,#2F95FF,#6DB4FF);-webkit-background-clip:text;background-clip:text;color:transparent}
.v .pill{align-self:flex-start;display:inline-flex;align-items:center;gap:14px;padding:12px 24px;border:1px solid rgba(109,180,255,.35);background:rgba(47,149,255,.08);border-radius:999px;color:#6DB4FF;font:600 22px 'Inter';letter-spacing:.14em;text-transform:uppercase}
.v .pill::before{content:'';width:10px;height:10px;border-radius:50%;background:#2F95FF;box-shadow:0 0 12px #2F95FF}
.v .lead,.v .list .item p,.v .card p{color:#94A3B8}
.v .lead strong{color:#fff}
.v .list .item{border-top:1px solid rgba(148,163,184,.16)}
.v .list .item:last-child{border-bottom:1px solid rgba(148,163,184,.16)}
.v .num{font:600 26px 'Inter Display';color:#2F95FF;width:52px;padding-top:9px;flex:0 0 52px}
.v .card{background:rgba(15,23,42,.65);border:1px solid rgba(148,163,184,.18)}
.v .card-tag{color:#6DB4FF}
.v .btn{background:#2F95FF;color:#fff;box-shadow:0 12px 44px rgba(47,149,255,.45)}
.v .cta-sub{color:#94A3B8}
.v .step{background:rgba(15,23,42,.65);border:1px solid rgba(148,163,184,.16);color:#fff}
.v .step span{background:rgba(47,149,255,.15);color:#6DB4FF;border:1px solid rgba(109,180,255,.35)}
.v .count,.v .bottom{color:#64748B}
.v .swipe{color:#6DB4FF}
.v .brand{display:flex;align-items:center;gap:16px}
.v .brand .m{height:40px}
.v .brand .w{height:17px;opacity:.95}
.v .mono-hero{position:absolute;right:20px;bottom:30px;width:470px;z-index:0}

/* ---------- UNNAR ---------- */
.u{background:#0E0D12;color:#EDE8DF}
.u .bg{position:absolute;inset:0;z-index:0;
  background:
   radial-gradient(circle at 92% 0%, rgba(200,152,46,.16), transparent 42%),
   radial-gradient(circle at 0% 100%, rgba(200,152,46,.07), transparent 45%)}
.u h1{font-family:'Gelasio';font-weight:400;font-size:96px;line-height:1.08;letter-spacing:-.01em;color:#EDE8DF}
.u h2{font-family:'Gelasio';font-weight:400;font-size:74px;line-height:1.1;color:#EDE8DF}
.u h3{font-family:'Inter';font-weight:600;color:#EDE8DF}
.u em{font-style:italic;color:#C8982E}
.u .eyebrow{font:600 22px 'Inter';letter-spacing:.18em;text-transform:uppercase;color:#C8982E}
.u .lead,.u .list .item p,.u .card p{color:#9088A0}
.u .lead strong,.u .list .item p.big{color:#EDE8DF}
.u .lead strong{font-weight:600}
.u .list .item{border-top:1px solid rgba(144,136,160,.2)}
.u .list .item:last-child{border-bottom:1px solid rgba(144,136,160,.2)}
.u .num{font:italic 400 40px 'Gelasio';color:#C8982E;width:64px;flex:0 0 64px}
.u .card{background:#19181F;border:1px solid #2A2733}
.u .card-tag{color:#C8982E}
.u .btn{background:#C8982E;color:#141008;box-shadow:0 12px 44px rgba(200,152,46,.3)}
.u .shot{border:1px solid #2A2733;box-shadow:0 30px 90px rgba(0,0,0,.65)}
.u .phone{background:#19181F;border:1px solid #2A2733;box-shadow:0 30px 90px rgba(0,0,0,.65)}
.u .note{color:#5E5870}
.u .count,.u .bottom{color:#5E5870}
.u .swipe{color:#C8982E}
.u .brand{display:flex;align-items:center;gap:16px}
.u .brand .mk{width:52px;height:52px;border-radius:13px;background:#2A2214;border:1px solid rgba(200,152,46,.28);display:flex;align-items:center;justify-content:center;font:400 36px 'Gelasio';color:#C8982E;padding-bottom:3px}
.u .brand .nm{font:400 36px 'Gelasio';color:#EDE8DF}
"""

def brand_html(b):
    if b == "v":
        return f'<div class="brand"><img class="m" src="{A}vorinn-monograma-alpha.png"><img class="w" src="{A}vorinn-wordmark-alpha.png"></div>'
    return '<div class="brand"><div class="mk">U</div><div class="nm">Unnar</div></div>'

def page(post, i, total, inner):
    b = post["brand"]
    is_cover = ('mono-hero' in inner) or ('shot-cover' in inner)
    wm = ''
    if i == 0 and not is_cover:
        wm = '<div class="wm-u">U</div>' if b == 'u' else f'<img class="wm-v" src="{A}vorinn-monograma-alpha.png">'
    left = "Vorinn Tecnologia" if b == "v" else "Unnar · um produto Vorinn"
    right = '<div class="swipe">Arraste <span style="font-size:30px">→</span></div>' if (i == 0 and total > 1) else '<div>@vorinn.com.br</div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="slide {b}"><div class="bg"></div>{'<div class="grid"></div>' if b=='v' else ''}
<div class="top">{brand_html(b)}<div class="count">{i+1}/{total}</div></div>
{wm}<div class="content{' cover' if is_cover else ''}">{inner}</div>{'<div class="fade"></div>' if 'shot-cover' in inner else ''}
<div class="bottom"><div>{left}</div>{right}</div>
</div></body></html>"""

def main(only=None):
    with sync_playwright() as p:
        import os
        exe = os.environ.get("CHROME_PATH")  # no claude.ai: /usr/bin/google-chrome
        br = p.chromium.launch(executable_path=exe, args=["--no-sandbox", "--allow-file-access-from-files"]) if exe else p.chromium.launch(args=["--allow-file-access-from-files"])
        pg = br.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for post in POSTS:
            if only and post["id"] not in only:
                continue
            d = OUT / post["id"]; d.mkdir(exist_ok=True)
            for f in d.glob("*.png"): f.unlink()
            n = len(post["slides"])
            for i, inner in enumerate(post["slides"]):
                html = page(post, i, n, inner)
                hp = d / f"slide-{i+1}.html"
                hp.write_text(html, encoding="utf-8")
                pg.goto(hp.as_uri()); pg.wait_for_load_state("networkidle")
                pg.evaluate("document.fonts.ready")
                pg.screenshot(path=str(d / f"{i+1:02d}.png"))
                hp.unlink()
            (d / "legenda.md").write_text(post["caption"], encoding="utf-8")
            print("ok", post["id"], n)
        br.close()

if __name__ == "__main__":
    main(sys.argv[1:] or None)
