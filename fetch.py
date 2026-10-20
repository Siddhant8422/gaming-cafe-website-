import urllib.request
import re

url = "https://pin.it/bFvq3TwfE"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        match = re.search(r'<meta property="og:image" content="(.*?)"', html)
        if match:
            print("FOUND IMAGE:", match.group(1))
        else:
            print("NO IMAGE TAG FOUND.")
except Exception as e:
    print("ERROR:", e)
