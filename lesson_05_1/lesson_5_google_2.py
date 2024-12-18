# Клик по кнопке без ID
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Открыть сайт
driver.get("http://uitestingplayground.com/dynamicid")
# Нажатие синей кнопки и повторение нажатия три раза
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, "button[class=\
        'btn btn-primary']").click()
    sleep(1)
    field = driver.find_element(By.CSS_SELECTOR, "div[class=\
        'container']").click()
    sleep(2)
# Закрыть браузер
driver.close()
