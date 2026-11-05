from PIL import Image, ImageDraw
import os
RES = "android/app/src/main/res"
BG = (1, 75, 200)
src = Image.open("icon-512.png").convert("RGB")
mask = Image.open("maskable-512.png").convert("RGB")
legacy = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
fore = {"mdpi": 108, "hdpi": 162, "xhdpi": 216, "xxhdpi": 324, "xxxhdpi": 432}
for d, s in legacy.items():
    folder = os.path.join(RES, "mipmap-" + d)
    os.makedirs(folder, exist_ok=True)
    img = src.resize((s, s), Image.LANCZOS)
    img.save(os.path.join(folder, "ic_launcher.png"))
    m = Image.new("L", (s * 4, s * 4), 0)
    ImageDraw.Draw(m).ellipse((0, 0, s * 4 - 1, s * 4 - 1), fill=255)
    m = m.resize((s, s), Image.LANCZOS)
    rnd = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    rnd.paste(img, (0, 0), m)
    rnd.save(os.path.join(folder, "ic_launcher_round.png"))
for d, s in fore.items():
    folder = os.path.join(RES, "mipmap-" + d)
    os.makedirs(folder, exist_ok=True)
    canvas = Image.new("RGB", (s, s), BG)
    inner = int(s * 0.84)
    canvas.paste(mask.resize((inner, inner), Image.LANCZOS), ((s - inner) // 2, (s - inner) // 2))
    canvas.save(os.path.join(folder, "ic_launcher_foreground.png"))
os.makedirs(os.path.join(RES, "values"), exist_ok=True)
open(os.path.join(RES, "values", "ic_launcher_background.xml"), "w").write(
    '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#014BC8</color>\n</resources>\n')

for n in ("ic_launcher", "ic_launcher_round"):
    for v in ("mipmap-anydpi-v26", "mipmap-anydpi-v33"):
        os.makedirs(os.path.join(RES, v), exist_ok=True)
        open(os.path.join(RES, v, n + ".xml"), "w").write(
            '<?xml version="1.0" encoding="utf-8"?>\n'
            '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
            '    <background android:drawable="@color/ic_launcher_background"/>\n'
            '    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>\n'
            '</adaptive-icon>\n')
print("icons done")
