from selene.support.shared import browser
from selene import be, have


def test_browser(open_browser):
    positive_case: str = 'selen'
    browser.element('[name="q"]').should(be.blank).type(positive_case).press_enter()

