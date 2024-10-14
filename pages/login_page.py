import allure

from data import User, Urls
from locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Клик на ссылку 'Восстановить пароль'")
    def click_reset_password_button(self):
        link = self.wait_and_find_element(LoginLocators.FORGOT_PASSWORD)
        link.click()

    @allure.step("Ввод электронной почты в поле 'Email'")
    def input_email_on_login_form(self):
        email = self.wait_and_find_element(LoginLocators.EMAIL)
        email.send_keys(User.user_data['email'])

    @allure.step("Ввод пароля в поле 'Пароль'")
    def input_password_on_login_form(self):
        password = self.wait_and_find_element(LoginLocators.PASSWORD)
        password.send_keys(User.user_data['password'])

    @allure.step("Нажатие на кнопку 'Войти'")
    def click_on_login_button(self):
        login = self.wait_and_find_element(LoginLocators.BUTTON_JOIN)
        login.click()

    def login(self):
        self.open_page(Urls.LOGIN_URL)
        self.input_email_on_login_form()
        self.input_password_on_login_form()
        self.click_on_login_button()
        self.wait_loading()