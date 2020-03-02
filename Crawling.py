import requests
from bs4 import BeautifulSoup
import time
import os
import datetime

dirname = './html_files'
if not os.path.exists(dirname):
    # 存在してなかったらディレクトリ作成
    os.mkdir(dirname)

url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&rn=0005"
response = requests.get(url)
time.sleep(1)
# ファイルに保存
page_count = 1    # ページ数のカウント
with open('./html_files/page{}.html'.format(page_count), 'w', encoding='utf-8') as file:
    file.write(response.text)

soup = BeautifulSoup(response.content, "html.parser")
print(int(soup.find('div', class_="paginate_set-hit").contents[0]))

while True:
    page_count += 1

    # 次のurlを探す
    next_url = soup.find("p", class_="pagination-parts")

    # 次ページがなくなったらbreakし終了
    if next_url == None:
        break

    # 次ページurlを取得しhtmlファイルとして保存
    url = "https://suumo.jp" + next_url.a.get('href')
    response = requests.get(url)
    time.sleep(1)
    with open('./html_files/page{}.html'.format(page_count), 'w', encoding='utf-8') as file:
        file.write(response.text)

    # 次ページのurlを取得するために解析準備
    soup = BeautifulSoup(response.content, "html.parser")

    # クローリング進捗の出力
    if page_count % 10 == 0:
        print(page_count, 'ページ取得')