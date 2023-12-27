import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import pprint

import requests

def download_all_htmls():
    htmls = []
    page_indices = range(0, 250, 25)
    #page_indices = list(range(0, 250, 25))

    for idx in page_indices:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        print("craw: ", url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        r = requests.get(url, headers=headers)
        #r = requests.get(url)

        #r = requests.get(url)
        if r.status_code != 200:
            raise Exception("请求失败")
            #print("error")
        htmls.append(r.text)

    return htmls


htmls = download_all_htmls()


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")

    article_items = (soup.find("div", class_="article")
                     .find("ol", class_="grid_view")
                     .find_all("div", class_="item"))
    data = []

    for article_item in article_items:
        rank = article_item.find("div", class_="pic").find("em").get_text()
        info = article_item.find("div", class_="info")
        title = info.find("div", class_="hd").find("span", class_="title").get_text()
        stars = (info.find("div", class_="bd")
                 .find("div", class_="star")
                 .find_all("span"))

        rating_star = stars[0]["class"][0]
        rating_num = stars[1].get_text()
        comments = stars[3].get_text()

        data.append({
            "rank:": rank,
            "display_rank": f"第{rank}名",
            "title": title,
            "rating_star": rating_star.replace("rating", "").replace("-t", ""),
            "rating_num": rating_num,
            "留言的人数": comments.replace("人评价", "")

        }
        )
    return data


import pprint

# Parse each HTML separately
for html in htmls:
    pprint.pprint(parse_html(html))

filex = []
for html in htmls:
    filex.extend(parse_html(html))


df = pd.DataFrame(filex)

df.to_excel("电影评分top250.xlsx")