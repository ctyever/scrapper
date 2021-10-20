from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


data = pd.read_csv('./data/nike5_url.csv')
for i in range(18):
    url = data.iloc[i, 0]
    print(url)