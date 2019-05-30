from behave import Given, when, then
from selenium.webdriver.common.by import By
from time import sleep


USER_EMAIL = (By.ID, 'user_email')
PASSWORD = (By.ID, 'user_password')
LOGIN_BTN = (By.CSS_SELECTOR, 'input.btn.btn-submit')



usernameStr = ['engineering@onboardiq.dev']
passwordStr = ['martiansworkingiq']

@Given('Open login page')
def open_page(context):
    context.driver.get("https://staging-with-es.herokuapp.com/users/sign_in")
    sleep(4)


@when('Input {email}')
def input_email(context, email,):
    context.driver.find_element(*USER_EMAIL).send_keys(usernameStr)
    sleep(2)


@then('Input {password}')
def input_password(context, password):
    context.driver.find_element(*PASSWORD).send_keys(passwordStr)
    sleep(2)


@when('Click LOG IN button')
def click_login(context):
    context.driver.find_element(*LOGIN_BTN).click()
    sleep(1)

