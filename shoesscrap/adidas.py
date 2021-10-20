from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class Adidas(object):

    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    new_ls = []
    union_ls = []
    dic = {}
    df = None

    def scrap(self):
        data = pd.read_csv('./data/football/adidas_football_list.csv')
        for i in range(55):
            url = data.iloc[i, 0]
        # url = 'https://shop.adidas.co.kr/PF020401.action?PROD_CD=FY0306'
            driver = webdriver.Chrome(self.driver_path)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
        # print(soup)
            all_div = soup.find_all(
                'div', {'class': 'thumbnails cut_thumbnails_wrap'})
        # print(all_div)
            self.new_ls = [i.find_all('img') for i in all_div]
        # print(self.new_ls)
            for i in self.new_ls[0]:
                if i == -1:
                    continue
                else:
                    print(i.get('src'))
            driver.close()


if __name__ == '__main__':
    adidas = Adidas()

    adidas.scrap()

#     def list_to_dictionary(self):
#         self.dic = dict(zip(range(1, 51), self.new_ls))
#
#     def dictionary_to_dataframe(self):
#         self.df = pd.DataFrame.from_dict(self.dic, orient='index')
#
#     def dataframe_to_csv(self):
#         path = './data/navermovie.csv'
#         self.df.to_csv(path, sep=',', na_rep='NaN')
#
# if __name__ == '__main__':
#     naver = Navermovie()
#
#     naver.scrap()
#     naver.list_to_dictionary()
#     naver.dictionary_to_dataframe()
#     naver.dataframe_to_csv()
