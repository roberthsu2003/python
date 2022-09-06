#!/usr/bin/python.3
'''
專門負責下載資料
'''
import json

def get_pm25():
    with open("空氣品質.json",mode="r",encoding="utf-8") as file:
        root = json.load(file)
        data_list = root["records"]
    return data_list
