# Модальное окно
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Открыть сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)
# В модальном окне нажмите на кнопку Сlose.
driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()
sleep(2)
# Закрыть браузер
driver.close()
