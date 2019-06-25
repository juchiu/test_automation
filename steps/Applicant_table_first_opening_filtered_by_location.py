from behave import When, then
from selenium.webdriver.common.by import By
from time import sleep



LINK_FIRST_CLICK = (By.CSS_SELECTOR, 'a.grouped-openings__locations-edit-link')
APPLICANT = (By.CSS_SELECTOR, 'a.dashboard-table__name-content.applicant-sidebar-toggle')
A_ACTIONS = (By.CSS_SELECTOR, 'button.applicant-profile-header__actions-toggle')

@Then('Click applicants in process link')
def Click_link(context):
    context.driver.find_element(*LINK_FIRST_CLICK).click()
    sleep(3)
@then('Click first applicant')
def Click_applicant(context):
    context.driver.find_element(*APPLICANT).click()
    sleep(4)

@then('Click_actions')
def Click_actions(context):
    context.driver.find_element(*A_ACTIONS).click()
    sleep(4)