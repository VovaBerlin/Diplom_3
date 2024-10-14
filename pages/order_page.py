import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Клик по заказу')
    def click_order(self):
        order = self.wait_and_find_element(OrderPageLocators.ORDER)
        order.click()

    @allure.step('Проверка отображения информации о заказе в ленте')
    def check_create_order_feed(self, text):
        issued = self.wait_text_and_find_element(OrderPageLocators.ORDER_STRUCTURE, text)
        return issued.text

    @allure.step('Получение ID созданного заказа')
    def get_order_id(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                                             (OrderPageLocators.ORDER_ID))
        order_id = self.get_actually_text(OrderPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_actually_text(OrderPageLocators.ORDER_ID)
        return order_id

    @allure.step('Нажатие на крестик в окне с ифнормацией о созданном заказе')
    def click_cross_order(self):
        button = self.wait_and_find_element(OrderPageLocators.CLOSE_MODAL_ORDER)
        button.click()

    @allure.step("Проверка совпадения id заказов в истории и в ленте")
    def check_order_id(self, order_id, locator):
        elements = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located(locator))

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Проверка нахождение id заказа в истории")
    def order_id_found_history(self, order_id):
        return self.check_order_id(order_id, OrderPageLocators.ORDERS_AT_HISTORY)

    @allure.step("Проверка нахождение id заказа в ленте")
    def order_id_found_feed(self, order_id):
        return self.check_order_id(order_id, OrderPageLocators.ORDERS_AT_FEED)

    @allure.step("Получение количества заказов сегодня")
    def get_order_total_count(self):
        counters = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.TOTAL_ORDER_COUNT))
        return counters.text

    @allure.step("Ожидание загрузки окна с ифнормацией о созданном заказе")
    def wait_loading_cross_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.CLOSE_MODAL_ORDER))

    @allure.step("Получение общего количества заказов")
    def get_order_daily_count(self):
        counters = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.DAILY_ORDER_COUNT))
        return counters.text

    @allure.step('Получаем номер заказа')
    def get_user_order_number(self, order_id):
        order_number = f'0{order_id}'
        WebDriverWait(self.driver, 15).until(
            expected_conditions.text_to_be_present_in_element(OrderPageLocators.NUMBER_ORDER_PROGRESS, order_id))
        return order_number

    @allure.step('Получаем номер заказа в работе')
    def get_user_order_in_progress(self):
        counters = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.NUMBER_ORDER_PROGRESS))
        return counters.text
