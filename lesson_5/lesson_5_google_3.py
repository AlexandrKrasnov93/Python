# Клик по кнопке с CSS-классом
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Открыть сайт
driver.get("http://uitestingplayground.com/classattr")
# Нажатие синей кнопки и повторить действия три раза
for _ in range(3):
    button = driver.find_element(By.XPATH, "//button[contains(concat(' ', \
normalize-space(@class), ' '), ' btn-primary ')]")
    button.click()
    sleep(2)
    driver.switch_to.alert.accept()
# Закрыть браузер
driver.close()
