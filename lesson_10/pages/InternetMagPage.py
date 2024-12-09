from selenium.webdriver.remote.webdriver import WebDriver


class InternetMagPage:
    """
    Класс для взаимодействия с интернет-магазином.

    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует InternetMagPage с веб-драйвером.

        """
        self.driver = driver

    def authorization(self, username: str, password: str) -> None:
        """
        Авторизует пользователя в интернет-магазине.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль пользователя.
        """

    def add_products(self) -> float:
        """
        Добавляет товары в корзину.

        Returns:
            float: Ожидаемая общая стоимость товаров.
        """

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        """

    def personal_data(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Вводит личные данные пользователя.

        Args:
            first_name (str): Имя пользователя.
            last_name (str): Фамилия пользователя.
            postal_code (str): Почтовый индекс.
        """

    def total_cost(self) -> float:
        """
        Получает фактическую общую стоимость товаров в корзине.

        Returns:
            float: Фактическая общая стоимость товаров.
        """

    def close(self) -> None:
        """
        Закрывает веб-драйвер.
        """
        self.driver.quit()
