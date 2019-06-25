from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


SEARCH_APPLICANTS = (By.ID, 'search')
LINK_FIRST_CLICK = (By.CSS_SELECTOR, 'a.grouped-openings__locations-edit-link')

@when('Click applicants in process')
def click_link(context):
    context.driver.find_element(*LINK_FIRST_CLICK).click()
    sleep(1)

@when('first search by {phone_number}')
def click_search_icon(context, phone_number):
    context.driver.find_element(*SEARCH_APPLICANTS).click()
    sleep(2)
    context.driver.find_element_by_id('search').send_keys('4155555555', Keys.ENTER)
    sleep(2)

@when('Search1 by {email}')
def click_search_icon1(context, email):
    context.driver.find_element(*SEARCH_APPLICANTS).click()
    sleep(1)
    context.driver.find_element_by_id('search').send_keys('margarita.chugunova@fountain.com', Keys.ENTER)
    sleep(3)

@when('Search2 {text}')
def click_search_icon2(context, text):
    context.driver.find_element(*SEARCH_APPLICANTS).click()
    sleep(1)
    context.driver.find_element_by_id('search').send_keys('test', Keys.ENTER)
    sleep(3)