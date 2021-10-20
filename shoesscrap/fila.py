from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class Fila(object):

    # url = 'https://www.nbkorea.com/product/productDetail.action?styleCode=NBPFBF701Y&colCode=30&cIdx=1288'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    new_ls = []
    union_ls = []
    dic = {}
    df = None

    def scrap(self):
        data = pd.read_csv('./data/sneakers/fila_sneakers_list.csv')
        for i in range(80):
            url = data.iloc[i, 0]

        # url = 'https://www.fila.co.kr/product/view.asp?ProductNo=43192'
            driver = webdriver.Chrome(self.driver_path)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup)
            all_div = soup.find_all('div', {'class': 'detail_img'})
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
    fila = Fila()

    fila.scrap()

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


