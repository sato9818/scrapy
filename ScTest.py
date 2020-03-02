import requests
from bs4 import BeautifulSoup
 
r = requests.get("https://suumo.jp")
print(r.content)
soup = BeautifulSoup(r.content, "html.parser")
 
# ニュース一覧を抽出
# print(soup.find("div", "sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"))