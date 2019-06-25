from behave import When, Then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert

HERI = (By.CSS_SELECTOR, 'td.obiq-table__cell.obiq-table__cell_name')
RECURRING_CHECKS = (By.CSS_SELECTOR, 'body > div.page__navigation > div > div > div:nth-child(1) > ul > li:nth-child(2) > a')
ADDRULE = (By.CSS_SELECTOR, 'button.obiq-button.obiq-button_primary')
RULENAME = (By.ID, 'title')

@When('Open posthire from top navbar')
def hover_over_and_select(context):
    element_to_hover_over = context.driver.find_element_by_css_selector('body > div.page__navigation > div > div > div:nth-child(2) > ul > li:nth-child(3) > div > button')
    hover = ActionChains(context.driver).move_to_element(element_to_hover_over)
    hover.perform()
    sleep(2)
    context.driver.find_element_by_xpath('/html/body/ul[2]/li[2]/a').click()
    sleep(3)

@Then('Click first applicant to verify page opened')
def verify_element_presented(context):
    context.driver.find_element(*HERI).click()
    sleep(2)

@When('click recurring checks')
def click_recurring_checks(context):
    context.driver.find_element(*RECURRING_CHECKS).click()

@When('Add rule')
def add_rule(context):
    context.driver.find_element(*ADDRULE).click()

@Then('Create new {rule}')
def fillout_form(context, rule):
    context.driver.find_element(*RULENAME).send_keys('test rule')
    sleep(2)

@Then("Select openings")
def select_opening(context):
    select_opening = context.driver.find_element_by_css_selector('div.Select-placeholder')
    hover2 = ActionChains(context.driver).move_to_element(select_opening).click()
    hover2.perform()
    context.driver.find_element_by_css_selector('div.Select-menu-outer').click()
    # print(select_opening.)
    sleep(2)
@Then('request document')
def request_document(context):
    request_document = context.driver.find_element_by_css_selector('div.Select-placeholder')
    hover3 = ActionChains(context.driver).move_to_element(request_document).click()
    hover3.perform()
    context.driver.find_element_by_css_selector('div.Select-menu-outer').click()
    sleep(2)

@Then('Select Type')
def select_type(context):
    select_type = context.driver.find_element_by_css_selector('div.Select-control')
    hover4 = ActionChains(context.driver).move_to_element(select_type).click()
    hover4.perform()
    context.driver.find_element_by_css_selector('div.Select-menu-outer').click()
    sleep(1)

@Then('Collect every month')
def collect_when(context):
    collect_when = context.driver.find_element_by_id('react-select-5--value')
    hover5 = ActionChains(context.driver).move_to_element(collect_when).click()
    hover5.perform()
    context.driver.find_element_by_css_selector('div.Select-menu-outer').click()
    sleep(4)

@Then('Click next')
def next(context):
    context.driver.find_element_by_css_selector('button.rule__button.obiq-button.obiq-button_primary').click()
    sleep(2)

@Then('Create')
def create(context):
    context.driver.find_element_by_css_selector('button.rule__button.obiq-button.obiq-button_primary').click()
    sleep(6)

