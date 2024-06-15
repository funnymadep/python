import requests

head = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' }
response = requests.get("http://books.toscrape.com/", headers = head)
if response.ok:
    print(response.text)
else:
    print('requests error')
