import math
import warnings
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import numpy as np

def convert_date(txt):
    if len(txt)!=0:
        if txt.split(" ")[1] in month_dict.keys():
            text_list = txt.split(" ")[1:]
            text_list[0] = month_dict[text_list[0]]
            str_date = text_list[0] + "-" + text_list[1][:-1] + "-" + text_list[2]
            return (str_date)
        else:
            return np.nan


warnings.filterwarnings("ignore")
driver = webdriver.Chrome(r'C:\Users\kovor\chromedriver\chromedriver.exe')
driver.get('https://www.giiresearch.com/material_report.shtml')
month_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07',
              'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
select = Select(driver.find_element_by_class_name('slct_limit'))
select.select_by_value('100')
total_elements = driver.find_element_by_xpath('//*[@id="BodySection"]/div[3]/div[2]/form/table[1]/tbody/tr/td[1]/b[3]')
total_elements = int(total_elements.text)
total_pages = math.ceil(total_elements / 100)

for i in range(total_pages):
    r = 2 + i
    date = driver.find_element_by_xpath('//*[@id="BodySection"]/div[3]/div[2]/form')
    tables = driver.find_elements_by_class_name('plist_item')
    dataframe = {'Title': [], 'PublishedBy': [], 'ProductCode': [], 'Date': [], 'Price': []}
    # df = pd.DataFrame(dataframe, columns=['Title', 'PublishedBy', 'ProductCode', 'Date', 'Price'], dtype=str)
    for j in range(len(tables)):
        text = tables[j].text.split("\n")
        dataframe['Title'].append(text[0])
        dataframe['PublishedBy'].append(' '.join(text[1].split(" ")[2:]))
        dataframe['ProductCode'].append(' '.join(text[2].split(" ")[2:]))
        dataframe['Date'].append(convert_date(text[3]))
        # data_list.append(text[4].split(" ")[2])
        dataframe['Price'].append(text[5].split(" ")[2])
    df = pd.DataFrame(dataframe)
    df.to_csv('D:\\output1.csv', mode="a", index=False, header=False)
    if i != total_pages:
        driver.find_elements_by_class_name('btn_next')[-1].click()

