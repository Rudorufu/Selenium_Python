# ⬆️⬇️ Применяем key_down() и key_up()
#
# 🔹 Задача: нажмите комбинацию клавиш CTRL + ALT + SHIFT + T, чтобы получить секретный пароль.
#
#     1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
#     2️⃣ Используя метод key_down(), создайте цепочку событий, которая имитирует зажатие клавиш CTRL + ALT + SHIFT + T.
#     3️⃣ Используя key_up() в той же цепочке событий, отожмите клавиши CTRL + ALT + SHIFT+T
#     4️⃣ Извлеките пароль из появившегося элемента с атрибутом key="access_code" и вставьте его в поле ниже между кавычками.
#
# 🟢Внимание тренажер работает только через Selenium.
# 💡Подсказка
#
# Так же можно нажать "T":
#
# .send_keys("T")
#
# 📌 Рекомендация
#
# После зажатия клавиш с помощью key_down() обязательно используйте key_up().
#
# ❓ Почему это важно?
#
# Метод .key_up() гарантирует корректную эмуляцию реального поведения пользователя.
# Если зажать комбинацию клавиш, но не отпустить их, это может привести к непредсказуемому поведению страницы или дальнейших тестов.
#
# Даже если в данном случае пароль можно получить без key_up(), правильная эмуляция нажатия и отпускания клавиш помогает
# избежать побочных эффектов и делает тесты более надёжными.
#
# Отпускать клавиши – это хороший тон в автоматизации! 🚀


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
url = "https://parsinger.ru/selenium/7/7.3.3/index.html"


with webdriver.Chrome() as browser:
    browser.get(url)
    actions = ActionChains(browser)
    actions.key_down(Keys.CONTROL)
    actions.key_down(Keys.ALT)
    actions.key_down(Keys.SHIFT)
    actions.key_down('T')
    actions.perform()
    actions.key_up(Keys.CONTROL)
    actions.key_up(Keys.ALT)
    actions.key_up(Keys.SHIFT)
    actions.key_up('T')
    actions.perform()
    print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)