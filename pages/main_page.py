import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPageLocators
from pages.base_page import BasePage



class MainPage(BasePage):
    @allure.step("Клик на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        button = self.wait_and_find_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        button.click()

    @allure.step("Клик на кнопку 'Лента Заказов'")
    def click_feed_orders_button(self):
        button = self.wait_and_find_element(MainPageLocators.FEED_BUTTON)
        button.click()

    @allure.step("Клик на кнопку 'Конструктор'")
    def click_constructor_button(self):
        button = self.wait_and_find_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        button.click()

    @allure.step("Клик на 'Флюоресцентная булка R2-D3'")
    def click_bun_button(self):
        button = self.wait_and_find_element(MainPageLocators.BUN_INGREDIENT)
        button.click()

    @allure.step("Клик на 'крестик' в деталях ингредиента")
    def click_cross_button(self):
        button = self.wait_and_find_element(MainPageLocators.EXIT_BUTTON)
        button.click()

    @allure.step("Проверка окна с деталями ингредиента")
    def check_ingredient_details(self, text):
        issued = self.wait_text_and_find_element(MainPageLocators.INGREDIENT_DETAILS, text)
        return issued.text

    @allure.step('Получение значения счетчика ингредиентов')
    def get_counter_ingredient_by_index(self):
        counters = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.INGREDIENT_COUNTER))
        return counters.text

    @allure.step("Проверить нахождение элемента на странице")
    def check_displayed_ingredient_details(self):
        check = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located
                                                     (MainPageLocators.INGREDIENT_DETAILS))
        return check.is_displayed()

    @allure.step('Проверить невидимость элемента')
    def check_invisibility_ingredient_details(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element
                                                    (MainPageLocators.INGREDIENT_DETAILS))


    @allure.step('Перетащить Флюоресцентную булку R2-D3')
    def add_filling_to_order(self):
        draggable = self.wait_and_find_element(MainPageLocators.BUN_INGREDIENT)
        droppable = self.wait_and_find_element(MainPageLocators.ORDER_BASKET)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_create_order_button(self):
        button = self.wait_and_find_element(MainPageLocators.CREATE_ORDER_BUTTON)
        button.click()

    @allure.step('Проверка создания заказа')
    def check_create_order(self, text):
        issued = self.wait_text_and_find_element(MainPageLocators.ORDER_IDENTIFIER, text)
        return issued.text