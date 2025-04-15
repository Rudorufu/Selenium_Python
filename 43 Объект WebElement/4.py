import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.1/index.html')
    button = browser.find_element(By.ID, "clickButton")
    time.sleep(2)
    button.click()
    time.sleep(10)