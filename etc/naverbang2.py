from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd


class Naverbang(object):
    def scrap(self):
        # try:
            data = pd.read_csv('./data/oneroom.csv')
            driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
            addrs = []
            code = data.loc[:2, '매물코드']
            print(len(code))
            for i in code:
                print(i)
                url = f'https://m.land.naver.com/article/info/{i}?newMobile'
                driver = webdriver.Chrome(driver_path)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                ls = soup.find('em', {'class': 'detail_info_branch'})
                print(ls)
                if ls != None:
                    newls = ls.text
                    addrs.append(newls)
                else:
                    addrs.append('')
                print(newls)
                addrs.append(newls)
                driver.close()
            # data['주소'] = addrs
            # data.to_csv('./saved_data/oneroom_add.csv')


Naverbang().scrap()