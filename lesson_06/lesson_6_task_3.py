# Дождаться картинки

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

# Перейти на сайт
driver.get("https://bonigarcia.dev/selenium- \
webdriver-java/loading-images.html")

# Дождиться загрузки всех картинок
element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape")))

# Получение значения атрибута src у 3-й картинки
src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

# Выводим значение в консоль
print(src)

# Закрыть браузер
driver.quit()
