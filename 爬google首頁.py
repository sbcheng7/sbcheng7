# import requests 套件包
import requests
# GET請求抓資料
page = requests.get('https://www.google.com.tw/')
# 印出網頁程式碼
print(page.text)
