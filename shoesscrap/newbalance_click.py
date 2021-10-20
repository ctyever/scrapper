from selenium import webdriver
import time


for i in range(100):
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    driver = webdriver.Chrome(driver_path)
    driver.get(
        "https://www.nbkorea.com/product/productList.action?cateGrpCode=250110&cIdx=1292")
    time.sleep(3)
    driver.find_elements_by_css_selector('.pro_area')[i].click()
    print(driver.current_url)
    driver.close()
