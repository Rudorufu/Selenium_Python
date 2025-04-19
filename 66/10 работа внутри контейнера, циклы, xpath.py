# 🎨 Операция: Ад цветовых шифров
#
# Приветствую, фанаты автоматизации и парсинга! Сегодня у нас не просто задание, а настоящий квест.
# Перед вами полотно веб-страницы, и ваша задача — расшифровать его, как настоящие криптографы цветов.
# Используя Selenium, вам нужно будет пройти через лабиринт элементов, собрать все цветовые коды и применить их для различных задач на странице.
# Что вас ждёт на странице.
#
#     50 уникальных контейнеров (div), каждый с собственным случайным фоновым HEX цветом.
#     В каждом блоке присутствует выпадающий список с множеством HEX цветов.
#     Кнопки с разными цветами и уникальным атрибутом data-hex=.
#     Чек-боксы и текстовые поля, которые также хотят участвовать в этой великой красочной головоломке.
#
# Что нужно сделать
#
#     Загрузка Страницы: Откройте страницу с помощью Selenium.
#
#         Используйте эту страницу с двумя элементами для тренировки.
#
#     Коды Цветов: Получите цвет в формате HEX из каждого элемента <span>.
#
#     Выбор в Списке: В выпадающем списке в каждом контейнере найдите и выберите тот же HEX цвет что и у родительского контейнера.
#
#     Кнопочная Магия: Найдите и нажмите на кнопку, у которой атрибут data-hex совпадает с HEX цветом родительского контейнера. !ты тут
#
#     Чек-Бокс Челлендж: Поставьте галочку в чек-боксе на странице.
#
#     Текстовое Поле: Вставьте в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.
#
#     Подтверждение: Нажмите на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".
#
#     Повторение: Повторите все эти шаги для каждого найденного на странице контейнера.
#
#     Финальный Шаг: После выполнения всех действий, нажмите на кнопку "Проверить все элементы", кнопка расположена в самом низу, появится alert если все условия соблюдены.
#
#     Секретный Код: Из алерт-окна получите числовой код и вставьте его в поле ответа степик.
#
# Примечания
#
#     Внимательно следите за атрибутами элементов, чтобы правильно их выбрать.
#     Код должен быть универсальным и работать со всеми найденными на странице элементами.


# Мой код
from selenium import webdriver
from selenium.webdriver.common.by import By
# url = 'https://parsinger.ru/selenium/5.5/5/test/test.html'
url = 'https://parsinger.ru/selenium/5.5/5/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    divs_global = browser.find_element(By.ID, 'main-container')
    divs = divs_global.find_elements(By.XPATH, './div')
    for i in divs:
        span = i.find_element(By.TAG_NAME, 'span').text
        i.find_element(By.TAG_NAME, 'select').send_keys(span)
        buttons = i.find_elements(By.TAG_NAME, 'button')
        for j in buttons:
            if j.get_attribute('data-hex') == span:
                j.click()
        i.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
        i.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys(span)
        i.find_element(By.XPATH, './button').click()
    browser.find_element(By.XPATH, './html/body/button').click()
    print(browser.switch_to.alert.text)


# Код препода:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
#
#
# with webdriver.Chrome() as driver:
#     driver.get("https://parsinger.ru/selenium/5.5/5/1.html")
#     wait = WebDriverWait(driver, 10)
#     containers = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[style*="background-color"]')))
#     for container in containers:
#         # Получаем HEX цвет из <span>
#         hex_color = container.find_element(By.TAG_NAME, 'span').text
#
#         # Выбираем соответствующий цвет в выпадающем списке
#         Select(container.find_element(By.TAG_NAME, 'select')).select_by_value(hex_color)
#
#         # Нажимаем на кнопку с атрибутом data-hex равным HEX цвету
#         container.find_element(By.CSS_SELECTOR, f'button[data-hex="{hex_color}"]').click()
#
#         # Ставим галочку в чек-боксе
#         container.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
#
#         # Вставляем HEX-цвет в текстовое поле
#         container.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(hex_color)
#
#         # Нажимаем кнопку "Проверить"
#         container.find_element(By.XPATH, './/button[text()="Проверить"]').click()
#
#     # Нажимаем кнопку "Проверить все элементы" внизу страницы
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Проверить все элементы"]'))).click()
#
#     # Ждем появления алерт-окна и получаем текст из него
#     alert = wait.until(EC.alert_is_present())
#     alert_text = alert.text
#     alert.accept()
#
#     # Извлекаем числовой код из текста алерта
#     secret_code = ''.join(filter(str.isdigit, alert_text))
#
# print(f'Секретный код: {secret_code}')