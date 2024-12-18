# Переименовать кнопку

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

# Перейти на сайт
driver.get(" http://uitestingplayground.com/textinput")

# Указать в поле ввода текст SkyPro
input_field = driver.find_element(By.CSS_SELECTOR, "#newButt \
onName").send_keys("SkyPro")

# Нажатие синей кнопки
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# Получиение текста кнопки
button_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).text

# Вывести в консоль (SkyPro)
print(button_text)

# Закрыть браузер
driver.quit()
