#  Применяем context_click() с кастомным контекстным меню.
#
# 🔹 Задача: выполните правый клик по заданному элементу, чтобы вызвать кастомное контекстное меню с вариантами.
# Затем выберите из этого меню пункт "Получить пароль" – именно этот выбор должен привести к появлению секретного пароля.
#
#     1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
#     2️⃣ Используя метод context_click(), выполните правый клик по элементу с id="context-area", чтобы отобразилось кастомное контекстное меню.
#     3️⃣ В появившемся меню, используя поиск по CSS-селектору, найдите пункт с атрибутом data-action="get_password" и кликните по нему.
#     4️⃣ Извлеките пароль из появившегося элемента с атрибутом key="access_code" и вставьте его в поле ниже между кавычками.
#
# 🟢 Внимание: тренажёр работает только через Selenium — кастомное меню активируется именно при эмуляции правого клика с WebDriver.
# 💡Подсказка
#
# Для вызова меню используйте ActionChains.context_click(), а для выбора пункта – не забудьте добавить time.sleep(),
# чтобы убедиться, что меню стало видимым, прежде чем выполнять клик по нужному пункту.
#
# Не пытайтесь просто применить click() на нужном пункте "Получить пароль" до вызова контекстного меню — это не сработает,
# так как он ещё не виден, пока вы не выполните context_click().


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
url = "https://parsinger.ru/selenium/7/7.3.4/index.html"


with webdriver.Chrome() as browser:
    browser.get(url)
    actions = ActionChains(browser)
    context = browser.find_element(By.ID,'context-area')
    actions.context_click(context).perform()
    get_pass = browser.find_element(By.CSS_SELECTOR, '[data-action="get_password"]')
    actions.click(get_pass).perform()
    print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)