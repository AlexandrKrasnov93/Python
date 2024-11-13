import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_main_class import shopMain
from shop_auth_class import shopBag
from shop_price import shopPrice


# тест магазина
@pytest.mark.webtest_3
def test_shop_main():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shop_main = shopMain(browser)
    shop_main.shop_auth()
    shop_main.shop_add()
# работа в корзине
    shop_bag = shopBag(browser)
    shop_bag.add_pay_phorm()
# проверка стоимости
    shop_price = shopPrice(browser)
    price = shop_price.shop_price()
    assert price == "58.29"
    browser.quit()
