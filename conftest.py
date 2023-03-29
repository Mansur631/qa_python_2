import selene
import selenium
from selenium import webdriver
from selene.support.shared import browser
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def install_webdriver():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return browser.config.driver


@pytest.fixture()
def open_browser(install_webdriver):
    browser.open('https://www.google.ru/?hl=ru')
