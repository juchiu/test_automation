from behave import when, then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SEARCH = (By.CSS_SELECTOR, 'i.fa.fa-search.global-nav-search__icon')

@when('search for applicant by {phone_number}')
def sss(context, phone_number):
    context.driver.find_element(*SEARCH).click()
    sleep(3)
    context.driver.find_element_by_id('query').send_keys('4155187685', Keys.ENTER)
    sleep(3)

@then('open first opening/stage')
def open_opening(context):
    context.driver.find_element_by_css_selector('#js-applicants-search__result > div.obiq-table > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > a').click()
    sleep(4)
@then('verify page opened')
def page_opened(context):
    applicant_name = context.driver.find_element_by_css_selector('a.dashboard-table__phone')
    assert applicant_name.text == '+1415-518-7685'
