import requests
from bs4 import BeautifulSoup
import os
def get_novel_chapters():
    root_url = "http://www.89wx.cc/7/7459/"
    r= requests.get(root_url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")


    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
           continue


        data.append(("http://www.89wx.cc/%s"%link['href'],link.get_text()))
    return data

"""
def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find("div", id = 'content').get_text()


for chapter in get_novel_chapters():
    url,title = chapter
    with open("%s.txt"%title, "w") as fout:
        fout.write(get_chapter_content(url))
    break
"""


def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, "html.parser")

    content_div = soup.find("div", id='content')

    if content_div:
        return content_div.get_text()
    else:
        print(f"未找到URL为 {url} 的内容")
        return None


def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, "html.parser")

    content_div = soup.find("div", id='content')

    if content_div:
        return content_div.get_text()
    else:
        print(f"未找到URL为 {url} 的内容")
        return None

novel_chapters = get_novel_chapters()
idx = 0

# 创建一个名为x的文件夹
output_folder = "斗破苍穹"
os.makedirs(output_folder, exist_ok=True)

for chapter in novel_chapters:
    idx += 1
    url, title = chapter
    content = get_chapter_content(url)

    if content is not None:
        # 将章节内容保存为单独的txt文件，并放入x文件夹
        file_path = os.path.join(output_folder, f"{title}.txt")
        with open(file_path, "w", encoding="utf-8") as fout:
            fout.write(content)
        print(f"第 {idx} 章节 {title} 已保存。")
    else:
        print(f"由于缺少内容，跳过 {title}。")

    # 如果要下载所有章节，请注释或删除下一行
    # break

print(f"所有内容已保存到 {output_folder} 文件夹中。")