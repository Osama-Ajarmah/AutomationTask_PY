import time

from selenium import webdriver
from selenium.webdriver import Keys





def googleResult(query):
    baseURL = "https://www.google.com"
    driver = webdriver.Chrome()
    driver.get(baseURL)

    try:
        driver.find_element("name","q").send_keys(query)
        driver.implicitly_wait(2)
        driver.find_element("name","btnK").send_keys(Keys.ENTER)
        time.sleep(2)
        result = driver.find_element("tag name", "h3")
        time.sleep(2)
        act_title =result.text

    except:
        act_title = "Can't find"
    driver.quit()
    return act_title