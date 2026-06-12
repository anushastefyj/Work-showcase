import urllib.request, json
req = urllib.request.Request("https://api.github.com/users/anushastefyj/repos?sort=updated&per_page=100", headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    print([r['name'] for r in data if r['name'] != 'anushastefyj'])
