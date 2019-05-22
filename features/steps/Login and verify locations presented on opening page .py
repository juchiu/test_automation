from behave import then
from selenium.webdriver.common.by import By
from time import sleep

ALL_LOCATIONS = (By.CSS_SELECTOR, 'div.obiq-flat-list.obiq-overlay-spinner')
ACTIONS_LABEL = (By.CSS_SELECTOR, 'div.grouped-openings__options-container')


@then("Every location on the page has 'applicants in process' text")
def verify_text(context):
   for x in context.driver.find_elements(*ALL_LOCATIONS):
        print('\nChecking:', x.text)
        assert 'applicants in process' in x.text, "Expected 'applicants in process' to be in location text, but got {}".format(x.text)
        assert 'approved' in x.text, "Expected 'approved' to be in location text, but got {}".format(x.text)
        assert 'in process' in x.text, "Expected 'in process' to be in location text, but got {}".format(x.text)


@then("Every location on the page has actions")
def verify_actions(context):
    #  """
    # Finds ALL location elements and searches for a action element inside each location element
    # Example:
    # # Get a location's element, it has html =>
    # x1_element = context.driver.find_elements(*ALL_LOCATIONS)[1]
    # print(x_element)
    # html = x1_element.get_attribute('innerHTML')
    # print(html)
    # # Search inside x1_element:
    # act = x1_element.find_element(*ACTIONS_LABEL)
    # print('\n', act.text)
    #  """
    actions = context.driver.find_elements(*ALL_LOCATIONS)
    for act in actions:
        print('\nAct element: ', act.text)
        act.find_element(*ACTIONS_LABEL)


