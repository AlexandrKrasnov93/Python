import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from task_1.auth_class import AuthPhorm
from task_1.auth_chek import authCheck
from task_2.calc_class import Calculator
from task_2.calc_res import Calcresult
from task_3.shop_main_class import shopMain
from task_3.shop_auth_class import shopBag
from task_3.shop_price import shopPrice

# форма авторизации


@pytest.mark.webtest_1
def test_auth_phorm():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    auth_phorm = AuthPhorm(browser)
    auth_phorm.add_auth_phorm()

# проверка цвета полей формы

    auth_check = authCheck(browser)
    color_Zip = auth_check.color_zip()
    assert color_Zip == "rgba(248, 215, 218, 1)"
    color_Adress = auth_check.color_adress()
    assert color_Adress == "rgba(209, 231, 221, 1)"
    color_Email = auth_check.color_email()
    assert color_Email == "rgba(209, 231, 221, 1)"
    color_Phone = auth_check.color_phone()
    assert color_Phone == "rgba(209, 231, 221, 1)"
    color_City = auth_check.color_city()
    assert color_City == "rgba(209, 231, 221, 1)"
    color_Country = auth_check.color_country()
    assert color_Country == "rgba(209, 231, 221, 1)"
    color_Jobpos = auth_check.color_jobpos()
    assert color_Jobpos == "rgba(209, 231, 221, 1)"
    color_Company = auth_check.color_company()
    assert color_Company == "rgba(209, 231, 221, 1)"
    browser.quit()

# тест калькулятора


@pytest.mark.webtest_2
def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    Calc = Calculator(browser)
    Calc.Calc_test()

# проверка результата калькулятора

    Calc_Res = Calcresult(browser)
    result = Calc_Res.result()
    assert result == "15"
    browser.quit()

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
