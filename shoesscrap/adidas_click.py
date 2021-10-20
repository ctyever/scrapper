from selenium import webdriver
import time


for i in range(100):
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    driver = webdriver.Chrome(driver_path)
    driver.get(
        "https://shop.adidas.co.kr/PF020201.action?S_CTGR_CD=01001001001001&STEP_YN=N&S_SIZE=&S_COLOR=&S_COLOR2=&S_PRICE=&S_STATE1=&S_STATE2=&S_STATE3=&NFN_ST=Y")
    time.sleep(3)
    driver.find_elements_by_css_selector('.link')[i].click()
    print(driver.current_url)
    driver.close()
