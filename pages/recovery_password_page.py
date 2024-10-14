import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ForgotPasswordLocators
from pages.base_page import BasePage


class RecoveryPasswordPage(BasePage):
    @allure.step("Ввод электронной почты в поле 'Email'")
    def input_email_for_reset_password(self, email):
        field = self.wait_and_find_element(ForgotPasswordLocators.INPUT_EMAIL)
        field.send_keys(email)

    @allure.step("Нажатие на кнопку 'Восстановить'")
    def click_recovery_button(self):
        button = self.wait_and_find_element(ForgotPasswordLocators.BUTTON_RESET)
        button.click()

    @allure.step("Нажатие на кнопку скрытия пароля в поле 'Пароль'")
    def click_show_password_button(self):
        button = self.wait_and_find_element(ForgotPasswordLocators.ICON_IN_FIELD_PASSWORD)
        button.click()

    def find_active_password_field(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                                                    (ForgotPasswordLocators.INPUT_ACTIVE))
