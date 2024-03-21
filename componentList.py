import requests 
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup

def listComponents(url):
    link_component_list = url
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

    requisicao = requests.get(link_component_list, headers=headers)

    site = BeautifulSoup(requisicao.text, "html.parser")

    component_list = []
    list = site.find_all("span", class_="ant-menu-title-content")

    for items in list:
        try:
            if "component" in items.find("a").get('href') and "overview" not in items.find("a").get('href'):
                component_list.append(items.find("a").get('href'))
        except:
            continue
    return component_list            

