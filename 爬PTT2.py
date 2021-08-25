import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
# 將網頁資料GET下來
soup = BeautifulSoup(r.text, "html.parser")
# 將網頁資料以html.parser
sel = soup.select("div.title a")
# 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel

for s in sel:
    print(s["href"], s.text)

fileOb = open('PTT_MobileComm.html', 'w', encoding='utf-8')
# 開啟一個檔案，沒有就新建一個
fileOb.write(htmldata())
fileOb.close()
