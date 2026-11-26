import sys, subprocess, pathlib
from playwright.sync_api import sync_playwright
html = pathlib.Path(sys.argv[1]).resolve()
mode = sys.argv[2]            # "frames" or "video"
out = pathlib.Path(sys.argv[3])
dur = float(sys.argv[4]) if len(sys.argv) > 4 else 20.0
times = [float(x) for x in sys.argv[5:]] if mode == "frames" else None
with sync_playwright() as p:
    import os
    exe = os.environ.get("CHROME_PATH")  # no claude.ai: /usr/bin/google-chrome
    br = p.chromium.launch(executable_path=exe, args=["--no-sandbox","--allow-file-access-from-files"]) if exe else p.chromium.launch(args=["--allow-file-access-from-files"])
    pg = br.new_page(viewport={"width":1080,"height":1920}, device_scale_factor=1)
    pg.goto(html.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
    if mode == "frames":
        out.mkdir(parents=True, exist_ok=True)
        for t in times:
            pg.evaluate(f"seek({t})"); pg.screenshot(path=str(out / f"t{t:05.2f}.jpg"), type="jpeg", quality=85)
    else:
        tmp = out.with_suffix(".tmp.mp4")
        ff = subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate","30","-c:v","mjpeg","-i","-",
                               "-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-movflags","+faststart",str(tmp)], stdin=subprocess.PIPE)
        n = int(round(dur*30))
        for i in range(n):
            pg.evaluate(f"seek({i/30})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        ff.stdin.close(); rc = ff.wait()
        if rc == 0: tmp.rename(out)
        print("rc", rc, n, "frames")
    br.close()
