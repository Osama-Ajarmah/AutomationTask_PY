import time

from selenium import webdriver
from selenium.webdriver import Keys




def yahooResult(query):
    baseURL = "https://www.yahoo.com"
    driver = webdriver.Chrome()
    driver.get(baseURL)
    try:
        driver.find_element("name","p").send_keys(query)
        driver.implicitly_wait(2)
        driver.find_element("id","ybar-search").send_keys(Keys.ENTER)
        time.sleep(2)
        result = driver.find_element("xpath","//h3/a")
        time.sleep(2)
        siteTitle = result.text
        driver.implicitly_wait(2)

    except:
        act_title = "Can't find"

    driver.quit()
    return siteTitle[15:36]