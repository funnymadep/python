import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}

num = 0;

for start_num in range(0, 250, 25):
    # print(start_num)

    response = requests.get(f'http://movie.douban.com/top250?start={start_num}', headers = headers)
    # print(response)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    span_title = soup.findAll("span", attrs={"class": "title"})
    for title in span_title:
        # print(title.string)
        title_string = title.string
        if "/" not in title_string:
            num += 1
            print(f'{num}: ' + title_string)
