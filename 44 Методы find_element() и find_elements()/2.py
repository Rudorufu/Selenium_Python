# 🔍 Каскадный поиск.
# 🔹 Задача: используя каскадный поиск найдите элемент на странице, кликните на него, и считайте появившийся атрибут в теге.
#     1️⃣ Зайти на сайт-тренажер с помощью Selenium.
#     2️⃣ Найти родительский элемент с идентификатором parent_id.
#     3️⃣ Внутри этого родительского элемента найти первый дочерний элемент с классом child_class и кликнуть его.
#     4️⃣ После клика в этом теге появится атрибут password, считать значение этого атрибута с помощью .get_attribute(), это и будет пароль.
#     5️⃣ Вставить полученный пароль в поле ниже между кавычек.
# 💡 Совет: выведите в print() значение атрибута password, чтобы потом без проблем ввести его на Stepik.


from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    parent_el = browser.find_element(By.ID, "parent_id")
    parent_el.find_element(By.CLASS_NAME, "child_class").click()
    pas = parent_el.find_element(By.CLASS_NAME, "child_class").get_attribute('password')
    browser.quit()
    print(pas)