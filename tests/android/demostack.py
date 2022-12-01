import allure
from allure import step
from selene import have
from selene.support.shared import browser


def test_add_to_cart():
    with allure.step('Open page and found item'):
        browser.open('https://bstackdemo.com/')
        browser.element('//*[@id="1"]/p').should(have.text('iPhone 12'))
    with allure.step('Add item to cart'):
        browser.element('//*[@id="1"]/div[4]').click()
    with allure.step('Item be in cart'):
        browser.element('//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').should(have.exact_text('iPhone 12'))