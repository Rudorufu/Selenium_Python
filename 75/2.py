#
#  Infinite scroll (Бесконечный скролл)
#
# Представьте себя хакером данных в виртуальном мире, где информация хранится не в обычных файлах, а в скрытых элементах на веб-страницах.
# Чтобы добраться до этой информации, вам нужно использовать Selenium и скрипт Python для автоматизации
# скроллинга по бесконечному списку элементов. Вам предстоит собрать все числа из этих элементов и сложить их.
# Цель
#
#     Инициализация: Используя Selenium, откройте заданный веб-сайт.
#     Скроллинг: На сайте имеется список из 100 элементов, который расширяется при скроллинге (infinity scroll).
#     Сбор данных: Скрольте по интерактивным элементам, чтобы раскрыть все 100 элементов списка. Используйте Keys.DOWN или методы ActionChains(driver).
#     Агрегация: Извлеките все числовые значения из этих элементов и сложите их.
#     Отправка ответа: Вставьте собранную сумму чисел в поле на Stepik.
#
#
# Подсказки и заметки
#
#     Помните о задержках при загрузке элементов.
#     Последний элемент списка имеет класс last-of-list. Используйте это для прерывания цикла скроллинга.
#     Внимательно изучите структуру HTML-страницы. Это поможет вам понять, как искать нужные элементы.


import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/infiniti_scroll_1/'

with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(2)
    list_input = []      # Инициализируем пустой список для хранения обработанных элементов ввода
    scroll_container = browser.find_element(By.ID, 'scroll-container')
    sums_2 = 0
    sum_of_spans = 0
    while sum_of_spans != sums_2 or sums_2 == 0:
        browser.execute_script("arguments[0].scrollBy(0, 250);", scroll_container)
        time.sleep(0.1)
        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        span_tags = [x for x in browser.find_elements(By.TAG_NAME, 'span')]
        # Обходим каждый элемент input в списке
        for tag_input in span_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                time.sleep(1)
                print(tag_input.text)
                time.sleep(1)
                sum_of_spans += int(tag_input.text)
                if sum_of_spans == sums_2:
                    break
                sums_2 = sum_of_spans
                # time.sleep(2)
                list_input.append(tag_input)       # Добавляем элемент в список обработанных элементов
    print(sum_of_spans)

# 916516