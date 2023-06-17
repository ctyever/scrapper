import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By


class CU:

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

        self.service = Service(ChromeDriverManager().install())

        self.page = 2

    def scrap(self, url):
        driver = webdriver.Chrome(service=self.service, options=self.options)

        driver.get(url)

        SCROLL_PAUSE_TIME = 1.5
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # (1) 4번의  스크롤링
            for i in range(4):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(SCROLL_PAUSE_TIME)
            try:
                # (2) 더보기 클릭 //*[@id="dataTable"]/div[4]/div[1] //*[@id="dataTable"]/div[2]/div[1]  //*[@id="dataTable"]/div[3]/div[1]
                driver.find_element(By.XPATH, f"//*[@id='dataTable']/div[{self.page}]/div[1]").click()
                self.page = self.page + 1
            except:
                print('End page')
                break

            # (3) 종료 조건
            # new_height = driver.execute_script("return document.body.scrollHeight")
            # if new_height == last_height:
            #     break
            # last_height = new_height
       
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # print(soup)

        name_div = soup.find_all('div', {'class': 'name'})
        price_div = soup.find_all('div', {'class': 'price'})

        # print(name_div)

        self.name_ls = [i.find('p').text for i in name_div]
        self.price_ls = [i.find('strong').text for i in price_div]

        print(f'name_len : {len(self.name_ls)}')
        print(f'price_len : {len(self.price_ls)}')
        driver.close()
    
    def list_to_dictionary(self):
        self.dic = dict(zip(self.name_ls, self.price_ls))

    def dictionary_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')

    def dataframe_to_csv(self, key):
        path = f'convenient_store_data/cu/{key}.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


if __name__=='__main__':

    url_dic = {
               'convenient_meal': 'https://cu.bgfretail.com/product/product.do?category=product&depth2=4&sf=N',
               'ready_to_eat': 'https://cu.bgfretail.com/product/product.do?category=product&depth2=4&depth3=2',
               'snack':'https://cu.bgfretail.com/product/product.do?category=product&depth2=4&depth3=3',
               'icecream':'https://cu.bgfretail.com/product/product.do?category=product&depth2=4&depth3=4',
               'food': 'https://cu.bgfretail.com/product/product.do?category=product&depth2=4&depth3=5',
               'beverage': 'https://cu.bgfretail.com/product/product.do?category=product&depth2=4&depth3=6',
               'house_goods': 'https://cu.bgfretail.com/product/product.do?category=product&depth2=4&depth3=7'
               }
    print(f'url_dic keys : {url_dic.keys()}')
    # print(type(url_dic.keys()))
    key_list = list(url_dic.keys())
    for key in key_list:
        url = url_dic[f'{key}']
        print(url)
        
        cu = CU()
        cu.scrap(url)
        cu.list_to_dictionary()
        cu.dictionary_to_dataframe()
        cu.dataframe_to_csv(key)
