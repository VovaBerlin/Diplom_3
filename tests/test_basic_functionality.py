import allure

from data import Urls, Text
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Переход по клику на "Конструктор"')
    def test_go_to_constructor(self, driver):
        constructor = MainPage(driver)
        constructor.open_page(Urls.LOGIN_URL)
        constructor.click_constructor_button()
        assert constructor.current_url == Urls.MAIN_URL

    @allure.title('Переход по клику на "Лента Заказов"')
    def test_go_to_feed_orders(self, driver):
        feed = MainPage(driver)
        feed.open_page(Urls.LOGIN_URL)
        feed.click_feed_orders_button()
        assert feed.current_url == Urls.FEED_URL

    #
    @allure.title('Проверка открытия окна с деталями ингредиентов')
    def test_show_details_ingredients(self, driver):
        details = MainPage(driver)
        details.open_page(Urls.LOGIN_URL)
        details.click_constructor_button()
        details.click_bun_button()
        assert details.check_ingredient_details(Text.DETAILS_INGREDIENTS) == Text.DETAILS_INGREDIENTS

    @allure.title('Клик на крестик закрывает окно с деталями инградиентов')
    def test_click_cross_exit_details_ingredients(self, driver):
        details = MainPage(driver)
        details.open_page(Urls.LOGIN_URL)
        details.click_constructor_button()
        details.click_bun_button()
        details.click_cross_button()
        details.check_invisibility_ingredient_details()
        assert details.check_displayed_ingredient_details() is False

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается.')
    def test_counter_increased(self, driver):
        counter = MainPage(driver)
        counter.open_page(Urls.MAIN_URL)
        pre_counter = counter.get_counter_ingredient_by_index()
        counter.add_filling_to_order()
        actual_counter = counter.get_counter_ingredient_by_index()
        assert pre_counter < actual_counter

    @allure.title('Залогиненный пользователь может оформить заказ.')
    def test_create_order_successful(self, driver):
        login = LoginPage(driver)
        login.login()
        order = MainPage(driver)
        order.add_filling_to_order()
        order.click_create_order_button()
        assert order.check_create_order(Text.CREATE_ORDER_TEXT) == Text.CREATE_ORDER_TEXT
