from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

count = 1
data = pd.read_csv('./data/football/newbal_football_url.csv')
for i in range(113):
    url = data.iloc[i, 0]
    urllib.request.urlretrieve(url, str(count) + ".jpg")
    count = count + 1