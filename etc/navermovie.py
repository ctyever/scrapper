from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


class Navermovie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    # driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    new_ls = []
    dic = {}
    df = None
    options = Options()
    options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

    service = Service(ChromeDriverManager().install())    


    def scrap(self):
        # driver = webdriver.Chrome(self.driver_path)
        driver = webdriver.Chrome(service=self.service, options=self.options)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class': 'tit3'})
        # print(all_div)
        self.new_ls = [i.find('a').text for i in all_div]
        driver.close()

    def list_to_dictionary(self):
        self.dic = dict(zip(range(1, 51), self.new_ls))

    def dictionary_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')

    def dataframe_to_csv(self):
        path = './data/navermovie.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


if __name__ == '__main__':
    naver = Navermovie()

    naver.scrap()
    naver.list_to_dictionary()
    naver.dictionary_to_dataframe()
    naver.dataframe_to_csv()
