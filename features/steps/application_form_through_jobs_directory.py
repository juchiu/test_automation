from behave import Given, When, Then
from selenium.webdriver.common.by import By
from time import sleep


COUNTRY = (By.ID, 'countryCode')
SELECT_OPTION = (By.CSS_SELECTOR, 'div.dropdown__menu.dropdown__menu_left.dropdown__menu_visible.select__dropdown-menu')
COMPANY = (By.ID, 'brandSlug')
SELECT_COMPANY = (By.CSS_SELECTOR, 'div.select-option')
SEARCH_BUTTON = (By.CSS_SELECTOR, 'a.ax-button')

@Given('Open Jobs directory')
def open_page(context):
    context.driver.get("https://staging-with-es.herokuapp.com/c/test_account/picker")

@When('select_country')
def select_country(context):
    context.driver.find_element(*COUNTRY).click()

@When('select_US')
def select_US(context):
    context.driver.implicitly_wait(2)
    context.driver.find_element(*SELECT_OPTION).click()

@Then('Select company')
def select_company(context):
    context.driver.find_element(*COMPANY).click()
    sleep(1)

@Then('select_Fountain')
def select_fountain(context):
    context.driver.find_element(*SELECT_COMPANY).click()
    sleep(1)

@Then('And search openings in jobs directory')
def search_openings(context):
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(2)