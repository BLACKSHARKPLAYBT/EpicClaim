import requests
from bs4 import BeautifulSoup
import re
from numpy import number

url = "https://indienova.com/gamedb/list/121/p/1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
get = requests.get(url, headers=headers)
print(get.status_code) # 200 means it's working

text = re.findall('.*<img.*?title=".*">',get.text)
number = len(text)
print(number)
i = 0
for image in text:
    i = i + 1
    if i >= number:
        break
    # title is here.
    title = re.findall('title=".*">', image)
    title = title[0].replace('title="', '').replace('">', '')
    print(title)
    # image is here.
    img = re.findall('src=".*" ', image)
    img = img[0].replace('src="', '').replace('" ', '')
    img = img + "_webp"
    print(img)
