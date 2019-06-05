from behave import Given, when, then
from selenium.webdriver.common.by import By
from time import sleep


USER_EMAIL = (By.ID, 'user_email')
PASSWORD = (By.ID, 'user_password')
LOGIN_BTN = (By.CSS_SELECTOR, 'input.btn.btn-submit')


usernameStr = ['engineering@onboardiq.dev']
passwordStr = ['martiansworkingiq']

def send_keys(context, element, keys, delay=0.01):
    subject = context.driver.find_element(*element)
    subject.click()
    subject.clear()
    for key in keys:
        subject.send_keys(key)
        sleep(delay)

@Given('Open login page')
def open_page(context):
    #context.driver.get("https://staging-with-es.herokuapp.com/users/sign_in")
    context.driver.get("http://localhost:3000/users/sign_in")
    sleep(4)

@when('Input {email}')
def input_email(context, email):
    context.driver.find_element(*USER_EMAIL).send_keys(usernameStr)
    #send_keys(context, USER_EMAIL, "ABCDE", 0.1)
    sleep(10)


@then('Input {password}')
def input_password(context, password):
    context.driver.find_element(*PASSWORD).send_keys(passwordStr)


@when('Click LOG IN button')
def click_login(context):
    context.driver.find_element(*LOGIN_BTN).click()
    sleep(10)

