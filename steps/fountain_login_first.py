from behave import Given, when, then
from selenium.webdriver.common.by import By
from time import sleep


USER_EMAIL = (By.ID, 'user_email')
PASSWORD = (By.ID, 'user_password')
LOGIN_BTN = (By.CSS_SELECTOR, 'input.btn.btn-submit')
TROUBLE_SIGN_IN_LINK = (By.XPATH, "//a[contains(@href,'trouble_sign_in')]")

# def create_emails_list(email) -> list:
#     print(email)
#     return [usernameStr[0], usernameStr[1], usernameStr[2].format.(email)]
#
usernameStr = ['YYYYY']
passwordStr = ['XXXXXX']
# for x in range(4):
# # driver.find_element(*USER_EMAIL).send_keys(usernameStr.format(x))

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

#
# @then('fountain.com signin page opens')
# def verify_signin_opens(context):
#     context.driver.find_element(*LOGIN_BTN)
#     context.driver.find_element(*TROUBLE_SIGN_IN_LINK)
