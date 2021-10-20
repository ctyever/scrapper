# from _typeshed import NoneType
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class Nike(object):

    # url = 'https://www.nike.com/kr/ko_kr/t/men/fw/running/CW7121-004/ymae67/nike-react-miler-2'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    new_ls = []
    union_ls = []
    dic = {}
    df = None

    def scrap(self):
        data = pd.read_csv('./data/football/nike_football_list.csv')
        for i in range(67):
            url = data.iloc[i, 0]
            driver = webdriver.Chrome(self.driver_path)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_div = soup.find_all('div', {'class': 'prd-gutter'})
            # print(all_div)
            for i in all_div:
                if i.find('img'):
                    # print(i)
                    self.new_ls.append(i.find('img').get('data-product-image'))
                else:
                    continue
            # self.new_ls = [i.find('img').get('data-product-image')
            #                for i in all_div]
            # print(self.new_ls)
            self.union_ls.append(self.new_ls)

            def la_print(a):
                sa = ""
                for i in a:
                    sa = sa + i + "\n"
                return sa

            print(la_print(self.new_ls))
            driver.close()
        # print(self.union_ls)


if __name__ == '__main__':
    nike = Nike()

    nike.scrap()

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
