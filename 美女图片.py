"""
url : https://pic.netbian.com/4kmeinv/
爬取图片并下载

爬取网页的requests，
解析网页BeautifulSoup

"""

import requests
import time
from bs4 import BeautifulSoup
import os

os.makedirs("美女图片2", exist_ok=True)
def download_all_htmls():
    htmls = []
    page_indices = range(1, 2, 1)

    for idx in page_indices:
        if idx == 1:
            url = f"https://pic.netbian.com/4kmeinv/index.html"
        else:
            url = f"https://pic.netbian.com/4kmeinv/index_{idx}.html"
        print("craw: ", url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"请求失败，状态码：{response.status_code}")
            # 如果请求失败，等待一段时间再进行下一次请求
            time.sleep(5)
            continue

        htmls.append(response.text)

    return htmls

all_image_urls = []

htmls = download_all_htmls()

for html in htmls:
    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.select('div.slist img[src^="/uploads/"]')

    for img in imgs:
        # Get the original image link instead of the thumbnail link
        img_url = f"https://pic.netbian.com{img['src'].replace('thumb', 'img')}"
        all_image_urls.append(img_url)

# 为每个图片下载并保存
for img_url in all_image_urls:
    filename = os.path.basename(img_url)
    with open(f"美女图片2/{filename}", "wb") as f:
        resp_img = requests.get(img_url)
        f.write(resp_img.content)
        print(f"Downloaded: {filename}", img_url)


