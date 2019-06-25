from behave import when, Then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

SEARCH = (By.CSS_SELECTOR, 'i.fa.fa-search.global-nav-search__icon')

@when('Search by {phone_number}')
def click_search_icon(context, phone_number):
    context.driver.find_element(*SEARCH).click()
    sleep(3)
    context.driver.find_element_by_id('query').send_keys('4155187685', Keys.ENTER)
    sleep(3)


@when('assert')
def assert_text(context):
    element = context.driver.find_element_by_css_selector('div#js-applicants-search__counter > b')
    assert element.text == '4155187685'


@when('By {email}')
def click_search_icon2(context, email):
    context.driver.find_element(*SEARCH).click()
    sleep(3)
    context.driver.find_element_by_id('query').send_keys('margarita.chugunova@fountain.com', Keys.ENTER)
    sleep(3)


@when('assert to verify search by email success')
def assert_text2(context):
    element = context.driver.find_element_by_css_selector('div#js-applicants-search__counter > b')
    assert element.text == 'margarita.chugunova@fountain.com'


@Then('Search {text}')
def click_search_icon3(context, text):
    context.driver.find_element(*SEARCH).click()
    sleep(3)
    context.driver.find_element_by_id('query').send_keys('rita', Keys.ENTER)
    sleep(3)


@when('assert to verify search by text success')
def assert_text3(context):
    element = context.driver.find_element_by_css_selector('div#js-applicants-search__counter > b')

    assert element.text == 'rita'

@Then('Open first opening/stage from search results page')
def click_first_applicant(context):
    context.driver.find_element_by_css_selector('a.applicant-sidebar-toggle').click()
    sleep(4)

@Then('verify applicant details opened')
def aseert(context):
    applicant_details = context.driver.find_element_by_css_selector('div.applicant-profile-header__info-name')
    assert applicant_details.text == 'Rita'
