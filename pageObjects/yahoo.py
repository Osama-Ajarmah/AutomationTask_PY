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
        time.sleep(10)
        result = driver.find_element("xpath","//div[@id='web']/ol/li[2]/div/div/h3/a/span")
        driver.implicitly_wait(2)
        result.click()
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(2)
        act_title = driver.title
    except:
        act_title = "Can't find"

    driver.quit()
    return act_title