import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc_class import Calculator
from calc_res import Calcresult


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
