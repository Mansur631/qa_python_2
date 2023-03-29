from selene.support.shared import browser
from selene import be, have


def test_search_positive(open_browser):
    positive_case: str = 'selene'
    browser.element('[name="q"]').should(be.blank).type(positive_case).press_enter()
    browser.element('[id="search"]').should(have.text('Selene - Wikipedia'))


def test_search_negative(open_browser):
    negative_case: str = '2@#@#1331e31##@*!&^!#&'
    browser.element('[name="q"]').should(be.blank).type(negative_case).press_enter()
    browser.element('[id="rcnt"]').should(have.text('По запросу - 2@#@#1331e31##@*!&^!#& -  ничего не найдено.'))

