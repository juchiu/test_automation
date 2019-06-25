from behave import When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import ActionChains


@When('select first dropdown')
def click_dropdown(context):
    menu = context.driver.find_element_by_css_selector('button.obiq-dropdown__toggle.global-nav__item-content.global-nav__item-content_link-dropdown.js-obiq-dropdown__toggle')
    hidden_submenu = context.driver.find_element_by_css_selector('body > div.obiq-dropdown__menu.js-obiq-dropdown__menu.global-nav__dropdown-items')

    actions = ActionChains(context.driver)
    actions.move_to_element(menu)
    # actions.click(hidden_submenu)
    actions.perform()

    # for element in hidden_submenu:
    #     print(element.text)
    #     sleep(2)