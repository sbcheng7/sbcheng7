import requests #是程式對網頁請求所需要的套件
from bs4 import BeautifulSoup
import pandas as pd #是轉換 dataframe 的好工具,非常建議學這個使用方式

r = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html")
    #透過get()方法(Method)存取網址
print(r.text)  
    #輸出排版後的HTML內容



