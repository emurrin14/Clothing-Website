import urllib.request
url='http://127.0.0.1:8000/static/clothesshop/css/websitestylesheet.css'
req=urllib.request.Request(url)
try:
    with urllib.request.urlopen(req, timeout=5) as r:
        print('STATUS', r.status)
        print(r.read(200).decode('utf-8', errors='replace'))
except Exception as e:
    print('ERROR', repr(e))
    raise SystemExit(1)
