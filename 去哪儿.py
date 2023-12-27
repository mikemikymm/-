# 发送网络请求的模块
import requests
# 解析数据的模块
import parsel
import csv
import time
import random
page_indices = range(0, 10, 1)
list(page_indices)


url = f'https://travel.qunar.com/travelbook/list.htm?page=1&order=hot_heat'



# <Response [200]>: 告诉我们 请求成功了
response = requests.get(url)
html_data = response.text
# html_data: 字符串
# 我们现在要把这个字符串 变成一个对象
selector = parsel.Selector(html_data)
# ::attr(href) url_list:列表
url_list = selector.css('.b_strategy_list li h2 a::attr(href)').getall()

# 保存成csv
csv_qne = open('去哪儿1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_qne)
# 写入数据
csv_writer.writerow(['地点', '短评', '出发时间', '天数', '人均消费', '人物', '玩法', '浏览量'])
"""
for detail_url in url_list:
    # 字符串的替换方法
    detail_id = detail_url.replace('/youji/', '')
    url_1 = 'https://travel.qunar.com/travelbook/note/' + detail_id
    print(url_1)

    # 发送请求到详情页面
    response_1 = requests.get(url_1).text
    selector_1 = parsel.Selector(response_1)

    # 提取数据
    #title = selector_1.css('.b_crumb_cont *:nth-child(3)::text').get().replace('旅游攻略', '')
    title = selector_1.css('.b_crumb_cont *:nth-child(3)::text').get()
    print("Title Element:", title)

    comment = selector_1.css('.title.white::text').get()
    date = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.when > p > span.data::text').get()
    days = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howlong > p > span.data::text').get()
    money = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howmuch > p > span.data::text').get()
    character = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.who > p > span.data::text').get()
    play_list = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.how > p > span.data span::text').getall()
    play = ' '.join(play_list)
    count = selector_1.css('.view_count::text').get()
    print(title, comment, date, days, money, character, play, count)

    # 写入CSV文件
    csv_writer.writerow([title, comment, date, days, money, character, play, count])
"""


for detail_url in url_list:
    # 字符串的替换方法
    detail_id = detail_url.replace('/youji/', '')
    url_1 = 'https://travel.qunar.com/travelbook/note/' + detail_id
    print(url_1)

    # 发送请求到详情页面
    response_1 = requests.get(url_1).text
    selector_1 = parsel.Selector(response_1)

    try:
        # 提取数据
        title = selector_1.css('.b_crumb_cont *:nth-child(3)::text').get()
        print("Title Element:", title)
        comment = selector_1.css('.title.white::text').get()
        date = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.when > p > span.data::text').get()
        days = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howlong > p > span.data::text').get()
        money = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howmuch > p > span.data::text').get()
        character = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.who > p > span.data::text').get()
        play_list = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.how > p > span.data span::text').getall()
        play = ' '.join(play_list)
        count = selector_1.css('.view_count::text').get()
        print(title, comment, date, days, money, character, play, count)

        # 写入CSV文件
        csv_writer.writerow([title, comment, date, days, money, character, play, count])

    except Exception as e:
        print(f"Error processing {url_1}: {e}")
# 关闭CSV文件
csv_qne.close()
