import re,sys
APP_ID = sys.argv[1]
p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()
tag = '<meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="%s"/>' % APP_ID
if "com.google.android.gms.ads.APPLICATION_ID" not in s:
    s = re.sub(r"(<application[^>]*>)", r"\1\n        " + tag, s, count=1)
open(p, "w", encoding="utf-8").write(s)
print("manifest patched")
