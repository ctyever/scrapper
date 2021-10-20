from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class Newbalance(object):

    # url = 'https://www.nbkorea.com/product/productDetail.action?styleCode=NBPFBF701Y&colCode=30&cIdx=1288'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    new_ls = []
    union_ls = []
    dic = {}
    df = None

    def scrap(self):
        data = pd.read_csv('./data/sandle/newbal_sandle_list.csv')
        for i in range(6):
            url = data.iloc[i, 0]
            # data = pd.read_csv('./data/nike4_listly.csv')
        # url = 'https://www.nbkorea.com/product/productDetail.action?styleCode=NBPFBF701Y&colCode=30&cIdx=1288'
            driver = webdriver.Chrome(self.driver_path)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_div = soup.find_all('div', {'class': 'thumb'})
        # print(all_div)
            self.new_ls = [i.find('img') for i in all_div[0]]
        # print(self.new_ls)
            for i in self.new_ls:
                if i == -1:
                    continue
                else:
                    print(i.get('src'))

            driver.close()


if __name__ == '__main__':
    newbalance = Newbalance()

    newbalance.scrap()

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
