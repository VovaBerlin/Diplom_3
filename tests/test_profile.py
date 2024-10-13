import allure

from data import Urls, User
from locators import ForgotPasswordLocators

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccPage
from pages.recovery_password_page import RecoveryPasswordPage


class TestPersonalAcc:
    @allure.title('Проверка на переход по клику на "Восстановить" пароль на странице логина')
    def test_go_to_password_recovery_page_by_clicking_recover_password_link(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_URL)
        login_page.click_reset_password_button()
        assert login_page.current_url == Urls.FORGOT_URL

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_enter_email_and_click_recovery_button(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page(Urls.FORGOT_URL)
        recovery_page.input_email_for_reset_password(User.user_data['email'])
        recovery_page.click_recovery_button()
        recovery_page.wait_and_find_element(ForgotPasswordLocators.ICON_IN_FIELD_PASSWORD)
        assert recovery_page.current_url == Urls.RESET_URL

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_show_password_button_activated_field(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page(Urls.FORGOT_URL)
        recovery_page.input_email_for_reset_password(User.user_data['email'])
        recovery_page.click_recovery_button()
        recovery_page.wait_and_find_element(ForgotPasswordLocators.ICON_IN_FIELD_PASSWORD)
        recovery_page.click_show_password_button()
        assert recovery_page.find_active_password_field()

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_go_to_personal_account(self, driver):
        login = LoginPage(driver)
        login.login()
        main_page = MainPage(driver)
        main_page.wait_loading()
        main_page.click_personal_account_button()
        main_page.wait_loading()
        assert main_page.current_url == Urls.PROFILE_URL

    @allure.title('Переход в раздел "История заказов"')
    def test_go_to_feed_orders(self, driver):
        login = LoginPage(driver)
        login.login()
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        personal_page = PersonalAccPage(driver)
        personal_page.click_order_history()
        assert main_page.current_url == Urls.ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self, driver):
        login = LoginPage(driver)
        login.login()
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        personal_page = PersonalAccPage(driver)
        personal_page.click_logout_account_button()
        personal_page.wait_loading_page()
        assert main_page.current_url == Urls.LOGIN_URL
