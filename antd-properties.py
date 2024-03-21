import requests 
import os
import sys
import pandas as pd
from componentList import listComponents
from bs4 import BeautifulSoup

comp_list = listComponents("https://ant.design/components/overview")
for items in comp_list:
    link = "https://ant.design" + items.lower()
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

    antd_request = requests.get(link, headers=headers)
    # print(antd_request)


    antd_page = BeautifulSoup(antd_request.text, "html.parser")
    table = antd_page.find("table", class_="component-api-table")
    comp_title = antd_page.find("div", class_="ant-flex-gap-small").find("div").get_text()
    print("processing " + comp_title)
    # print(table.prettify())
    # empty list
    data = []

    # for getting the header from
    # the HTML file
    list_header = []
    header = antd_page.find_all("table")[0].find("tr")

    for items in header:
        try:
            list_header.append(items.get_text())
        except:
            continue

    # for getting the data 
    HTML_data = antd_page.find_all("table")[0].find_all("tr")[1:]

    for element in HTML_data:
        sub_data = []
        for sub_element in element:
            try:
                sub_data.append(sub_element.get_text())
            except:
                continue
        data.append(sub_data)

    # Storing the data into Pandas
    # DataFrame 
    dataFrame = pd.DataFrame(data = data, columns = list_header)

    # Converting Pandas DataFrame
    # into CSV file
    dataFrame.to_csv('components/' + comp_title + '.csv')