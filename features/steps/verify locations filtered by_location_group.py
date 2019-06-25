from behave import then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

ALL_LOCATIONS_new = (By.CSS_SELECTOR, 'div.obiq-flat-list.obiq-overlay-spinner')
DROPDOWN = (By.CSS_SELECTOR, 'div.Select-control')

@then('Click dropdown to see filtering options')
def click_dropdown(context):
    context.driver.find_element(*ALL_LOCATIONS_new).click()
    sleep(4)

@then('select by')
def select_option(context):
    el_to_hover_over = context.driver.find_element(*DROPDOWN)
    hover = ActionChains(context.driver).move_to_element(el_to_hover_over).click()
    hover.perform()
    sleep(1)
    context.driver.find_elements_by_css_selector('div.Select-menu-outer')[-1].click()
    sleep(4)
@then('verify select by location group')
def verify_text(context):
    by_location_group = context.driver.find_element_by_css_selector('input.obiq-input.location-groups-dropdown__input.obiq-input_full-width').click()
    by_location_group = context.driver.find_element_by_css_selector('div.obiq-dropdown__item-content')
    assert by_location_group.text == 'California'
