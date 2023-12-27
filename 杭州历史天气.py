import requests
import pandas as pd

url = "https://tianqi.2345.com/Pc/GetHistory"

headers = {
    "User-Agent" : """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"""
}


def craw_table(year, month):
  """提供年份和月份，爬取对应的表格数据"""
  parameters = {
        "areaInfo[areaId]": 58457,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month,
    }

  response = requests.get(url, headers=headers, params=parameters)
  data = response.json()["data"]
  df = pd.read_html(data)[0]
  return df

#df = craw_table(2022,3)
#print(df.head())

df_list = []

for year in range(2011, 2022):
    for month in range(1, 13):

        print("爬取： ", year, month)

        df = craw_table(year, month)
        # df = craw_table(2023, 1)
        # print(df)
        df_list.append(df)

pd.concat(df_list).to_excel("杭州历史天气查询.xlsx", index = False)






