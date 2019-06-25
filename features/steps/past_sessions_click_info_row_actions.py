from behave import When, Then
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from time import sleep

SESSIONS = (By.CSS_SELECTOR, "a.global-nav__item-content.global-nav__item-content_link")


@When ('Click sessions')
def click_sessions(context):
    hewrtest = context.driver.find_element_by_css_selector('ul.global-nav__items')
    hewrtest = hewrtest.find_element_by_css_selector('body > div.page__navigation > div > div > div:nth-child(1) > ul > li:nth-child(3) > a').click()
    sleep(4)

@When('Click past')
def click_past(context):
    context.driver.find_element_by_css_selector('#scheduled-sessions > div > main > div > div.scheduled-sessions__content-headers > div.scheduled-sessions__top-buttons-row > div.obiq-buttons-group.scheduled-sessions__time-filter.obiq-buttons-group_theme_outline-secondary > button:nth-child(1)').click()
    sleep(2)

@When('Verify past sessions')
def find_sessionlist(context):
    find_sessionlist = context.driver.find_elements_by_css_selector('div.scheduled-sessions__list')
    print('find_sessionlist.format(elements)')
    sleep(2)

@Then('Click info row actions')
def actions(context):
    # context.driver.find_elements_by_css_selector('div.scheduled-session__info-row-actions')
    context.driver.find_element_by_css_selector('#scheduled-sessions > div > main > div > div.scheduled-sessions__container > div:nth-child(1) > div > div.scheduled-session__info-row > div > button:nth-child(1)').click()
    sleep(2)

@Then('Close manage applicants modal')
def close_manage_applicant_modal(context):
    context.driver.implicitly_wait(3)
    context.driver.find_element_by_css_selector('body > div.obiq-modal.obiq-modal_size_big > div > div > button').click()
    sleep(2)

@Then('Click info row actions and close')
def edit_a(context):
        # context.driver.find_elements_by_css_selector('div.scheduled-session__info-row-actions')
    context.driver.find_element_by_css_selector('#scheduled-sessions > div > main > div > div.scheduled-sessions__container > div:nth-child(1) > div > div.scheduled-session__info-row > div > button:nth-child(2)').click()
    sleep(4)
    context.driver.find_element_by_css_selector('body > div.obiq-modal.obiq-modal_size_small > div > div > footer > button.obiq-footer-buttons__button.obiq-button.obiq-button_secondary').click()
    sleep(2)

@Then('Export')
def export(context):
    context.driver.find_element_by_css_selector('#scheduled-sessions > div > main > div > div.scheduled-sessions__container > div:nth-child(1) > div > div.scheduled-session__info-row > div > a').click()
    sleep(4)
