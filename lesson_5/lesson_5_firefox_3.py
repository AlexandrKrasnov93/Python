# Форма авторизации
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Открыть сайт
driver.get("http://the-internet.herokuapp.com/login")
# Ввод в поле username значение "tomsmith"
driver.find_element(By.ID, "username").send_keys("tomsmith")
sleep(2)
# Ввод в поле password значение "SuperSecretPassword!"
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(2)
# Нажатие кнопку Login
button = driver.find_element(By.TAG_NAME, "button").click()
sleep(2)
# Закрыть браузер
driver.close()
