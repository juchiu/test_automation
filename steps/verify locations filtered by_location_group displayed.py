from behave import then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import Select

ALL_LOCATIONS_new = (By.CSS_SELECTOR, 'div.obiq-flat-list.obiq-overlay-spinner')
# ALL_NEW = (By.CSS_SELECTOR, 'div.Select-control')
# ACTIONS_LABEL = (By.CSS_SELECTOR, 'div.grouped-openings__options-container')
# LOCATION_GROUP_HEADER = (By.CSS_SELECTOR, 'h5.openings-view__location-group-header')
# OPTIONS = (By.CSS_SELECTOR, 'span#react-select-2--value-item.Select-value-label')
# OPTIONS = (By.XPATH, "//div[@class='select-menu-outer']/span[@role='option' and contains(@id,'2')]")
TEST1 = (By.XPATH, "//div[@aria-owns=react-select-2--list and@aria-activedescendant='react-select-2--option-1']")

@then('Click dropdown to see filtering options')
def click_dropdown(context):
    context.driver.find_element(*ALL_LOCATIONS_new).click()
    sleep(4)

@then ('select by location group')
def select_option(context):
    context.driver.find_element(*TEST1)

    # dropdown = driver.find_elements******
    # Select(dropdown).select_by_index




    # dropdown = driver.find_elements******
    # Select(dropdown).select_by_index

# @then('Wait and select by location group')
# def see(context):
#     see = Select(context.driver.find_element_By_Xpath("//div[@class='select-control']")
#     #  # react-select-2--value-item'))
    # see.select_by_visible_text('By Location Group')
#
# @then ('Wait and select by location group')
# def select_option(context):
#     context.driver.find_element(*OPTIONS).click()
#     sleep(4)
#
#
# @then ('Verify filtered by_location_group')
# def verify_text(context):
#     kkk = context.driver.find_element(*LOCATION_GROUP_HEADER)
#     print('\nChecking:')
#     assert 'CALIFORNIA' in kkk.text, "Expected 'applicants in process' to be in location text, but got {}".format(kkk.text)
#         # assert 'approved' in x.text, "Expected 'approved' to be in location text, but got {}".format(x.text)
#         # assert 'in process' in x.text, "Expected 'in process' to be in location text, but got {}".format(x.text)

#
# @then("Every location on the page has actions")
# def verify_actions(context):
#     #  """
#     # Finds ALL location elements and searches for a action element inside each location element
#     # Example:
#     # # Get a location's element, it has html =>
#     # x1_element = context.driver.find_elements(*ALL_LOCATIONS)[1]
#     # print(x_element)
#     # html = x1_element.get_attribute('innerHTML')
#     # print(html)
#     # # Search inside x1_element:
#     # act = x1_element.find_element(*ACTIONS_LABEL)
#     # print('\n', act.text)
#     #  """
#     actions = context.driver.find_elements(*ALL_LOCATIONS)
#     for act in actions:
#         print('\nAct element: ', act.text)
#         act.find_element(*ACTIONS_LABEL)
