import time
from selenium import webdriver
from selenium.webdriver import Keys



def bingResult(query):
    baseURL = "https://www.bing.com"
    driver = webdriver.Chrome()
    driver.get(baseURL)
    try:
        driver.implicitly_wait(4)
        driver.find_element("name", "q").send_keys(query)
        time.sleep(6)
        osama = driver.find_element("name", "search")
        osama.submit()
        time.sleep(10)
        result = driver.find_element("xpath","/html/body/div[1]/main/ol/li[1]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/h2/a")
        time.sleep(10)
        result.click()
        time.sleep(2)
        act_title = driver.title
    except:
        act_title = "no data found"
    driver.quit()
    return act_title