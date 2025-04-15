import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    browser.find_element(By.ID, "codeInput").send_keys("Дрогон")
    button = browser.find_element(By.ID, "clickButton")
    time.sleep(2)
    button.click()
    time.sleep(10)