from behave import Given, When, Then
from selenium.webdriver.common.by import By
from time import sleep

FIRSTNAME = (By.ID, 'application_form_first_name')
LASTNAME = (By.ID, 'application_form_last_name')
EMAIL = (By.ID, 'application_form_email')
PHONENUMBER = (By.ID, 'application_form_phone_number')
SUBMIT = (By.CSS_SELECTOR, 'button.btn-apply.js-submit.app-apply-button.application-form__submit-button')


@Given('Open application form')
def open_page(context):
    context.driver.get("https://staging-with-es.herokuapp.com/test_account/apply/public-funnel?preview=true")

@When('Fill out application form')
def fill_out_form(context):
    context.driver.find_element(*FIRSTNAME).send_keys('rita')
    context.driver.find_element(*LASTNAME).send_keys('chu')
    context.driver.find_element(*EMAIL).send_keys('margarita.chugunova+123@fountain.com')
    context.driver.find_element(*PHONENUMBER).send_keys('4155555555')

@Then('Click submit')
def click_submit(context):
    context.driver.find_element(*SUBMIT).click()
    sleep(2)

@Then('Page opened')
def new_page(context):
    actual_text = context.driver.find_element_by_css_selector('div.panel-body__description')
    assert actual_text.text == "Please look for the next steps soon!"


