import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_loading(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(MainPageLocators.WAIT_WINDOW))

    def wait_and_find_element(self, locator):
        self.wait_loading()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def wait_text_and_find_element(self, locator, text):
        self.wait_loading()
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    def get_actually_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    @allure.step('Открыть страницу по адресу.')
    def open_page(self, url):
        self.driver.get(url)
        self.wait_loading()

    @property
    @allure.step('Получить текущий URL.')
    def current_url(self):
        return self.driver.current_url

