import time
from selenium import webdriver
from selenium.webdriver import Keys



def bingResult(query):
    baseURL = "https://www.bing.com"
    driver = webdriver.Chrome()
    driver.get(baseURL)
    try:
        driver.implicitly_wait(3)
        driver.find_element("name", "q").send_keys(query)
        time.sleep(3)
        osama = driver.find_element("name", "search")
        osama.submit()
        time.sleep(2)
        result = driver.find_element("tag name", "h2")
        time.sleep(2)
        act_title = result.text

    except:
        act_title = "no data found"
    driver.quit()
    return act_title