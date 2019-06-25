from time import sleep
from selenium.webdriver.support.ui import Select
from behave import When, Then

expected_text = ['Send Email', 'Send Text/SMS', 'Move to Next Stage', 'Move to Stage...', 'Reject...', 'Delete']
@When('Click applicants in process link2')
def Click_link(context):
    context.driver.implicitly_wait(2)
    context.driver.find_element_by_css_selector('a.grouped-openings__locations-edit-link').click()
    sleep(2)


@Then('Select two users')
def checkbox(context):
    context.driver.find_element_by_css_selector('body > div.page__content > div > div > div.js-dashboard-table > div > div.dashboard-table__table-container > table > thead > tr > th:nth-child(1) > div > label').click()
    context.driver.find_element_by_css_selector('#batch-selection__select-all')
    sleep(2)

@Then('Click Bulk Actions dropdown and verify actions')
def bulk_actions_dropdown(context):
    context.driver.find_element_by_css_selector('div.dashboard-table-toolbar__bulk-actions-dropdown.obiq-dropdown.js-obiq-dropdown').click()
    sleep(2)
    elements = context.driver.find_elements_by_css_selector('div.obiq-dropdown__menu.js-obiq-dropdown__menu.obiq-dropdown__menu_visible > button')
    for element in elements:
     assert element.text == expected_text[elements.index(element)]
     f'Expected {element.text} but got {expected_text[elements.index(element)]}'

