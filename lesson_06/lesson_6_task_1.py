# Нажать на кнопку

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

# Перейти на страницу
driver.implicitly_wait(20)
driver.get("http://www.uitestingplayground.com/ajax")

# Нажатие синей кнопки и получение текста
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# Вывести в консоль
print(txt)

# Закрыть браузер
driver.quit()
