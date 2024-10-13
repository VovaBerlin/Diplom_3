import pytest
from selenium import webdriver
from data import Urls
from pages.login_page import LoginPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()


    yield browser

    browser.quit()

