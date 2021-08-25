# -*- coding: utf-8 -*-
"""
Created on Mon May  4 01:59:51 2020
@author: Zino
dataset:https://data.gov.tw/dataset/120711
"""
# 導入模組(module)
import requests
import json

# 1.2. 對網址get後 存在response變數中
response = requests.get(
    "https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json")
# 3. 使用json module讀取 Json 資料格式
jd = json.loads(response.text)
# 操作List 印出第一比資料
print(jd[0])
