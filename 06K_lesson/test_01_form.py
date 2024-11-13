import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from auth_class import AuthPhorm
from auth_chek import authCheck


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
