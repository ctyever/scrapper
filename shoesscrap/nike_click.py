from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get("https://www.nike.com/kr/ko_kr/w/men/fw/running")
time.sleep(6)
driver.find_elements_by_css_selector('.category-overlaytext')[0].click()