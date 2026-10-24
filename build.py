"""Erzeugt index.html (installierbare PWA) aus app.html. Aufruf: python3 build.py"""
import re, pathlib
here = pathlib.Path(__file__).parent
body = (here / 'app.html').read_text()
# Lernplan-Bibliothek lokal statt vom CDN, damit die App offline startet
body = body.replace('https://cdn.jsdelivr.net/npm/ts-fsrs@5.2.3/dist/index.umd.js', 'vendor/ts-fsrs.umd.js')
body = body.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
head = '''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Karten">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<link rel="icon" href="icons/icon-192.png">
</head>
<body>
'''
tail = '''
<script>
if('serviceWorker' in navigator){window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}))}
</script>
</body>
</html>
'''
(here / 'index.html').write_text(head + body + tail)
sw = here / 'sw.js'
t = sw.read_text()
m = re.search(r"zoes-karten-v(\d+)", t)
t = t.replace(m.group(0), f"zoes-karten-v{int(m.group(1)) + 1}")
sw.write_text(t)
print('index.html gebaut, Cache', f"v{int(m.group(1)) + 1}")
