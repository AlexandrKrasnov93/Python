import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage
from pages.InternetMagPage import InternetMagPage
from pages.PersonalDataPage import PersonalDataPage


@pytest.mark.webtest_1
@allure.feature("Персональные данные")
@allure.story("Отправка формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Отправка  формы с валидными данными")
@allure.description("Этот тест проверяет, что форма может быть отправлена с  валидными данными")
def test_personal_data_form():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        personal_data_page = PersonalDataPage(driver)

    with allure.step("Заполнение формы персональными данными"):
        personal_data_page.personal_data(
            name="Иван", last="Петров", address="Ленина, 55-3", email="test@skypro.com",
            phone="+7985899998787", city="Москва", country="Россия", job="QA", company="SkyPro"
        )

    with allure.step("Проверка цвета поля ZIP-кода"):
        assert personal_data_page.zip_code_red(), "Поле ZIP-кода должно быть красным"

    with allure.step("Проверка цвета других полей"):
        assert personal_data_page.other_fields_green(), "Другие поля должны быть зелеными"

    with allure.step("Закрытие браузера"):
        personal_data_page.close_driver()


@pytest.mark.webtest_2
@allure.feature("Калькулятор")
@allure.story("Операция сложения")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест операция сложения в калькуляторе")
@allure.description("Этот тест проверяет, правильно ли калькулятор выполняет сложение")
def test_addition_operation():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        calculator_page = CalculatorPage(driver)

    with allure.step("Установка задержки"):
        calculator_page.delay()

    with allure.step("Выполнение операции сложения"):
        calculator_page.perform_addition()

    with allure.step("Проверка результата. Ожидаемый результат сложения: 15"):
        assert calculator_page.get_result()

    with allure.step("Закрытие браузера"):
        calculator_page.close_driver()


@pytest.mark.webtest_3
@allure.id("Internet_mag")
@allure.epic("Интернет магазин")
@allure.severity(allure.severity_level.BLOCKER)
@allure.story("Покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара и оплата товара")
def test_form_internet_mag():
    with allure.step("Открытие страницы"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной с  классом InternetMagPage"):
        internet_mag_page = InternetMagPage(driver)

    with allure.step("Авторизация пользователя"):
        internet_mag_page.authorization("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        internet_mag_page.add_products()

    with allure.step("Переход в корзину"):
        internet_mag_page.go_to_cart()

    with allure.step("Ввод личных данных"):
        internet_mag_page.personal_data("Sanya", "Krasnov", "428000")

    with allure.step("Получение  стоимости товара"):
        internet_mag_page.total_cost()

    with allure.step("Закрытие браузера"):
        internet_mag_page.close()
