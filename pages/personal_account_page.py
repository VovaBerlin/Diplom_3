import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import UserProfilLocators, LoginLocators
from pages.base_page import BasePage


class PersonalAccPage(BasePage):
    @allure.step("Клик на кнопку 'История заказов'")
    def click_order_history(self):
        button = self.wait_and_find_element(UserProfilLocators.ORDER_HISTORY_BUTTON)
        button.click()

    @allure.step("Клик на кнопку 'Выход'")
    def click_logout_account_button(self):
        button = self.wait_and_find_element(UserProfilLocators.LOGOUT_BUTTON)
        button.click()

    def wait_loading_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                                             (LoginLocators.BUTTON_JOIN))
