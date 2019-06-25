from time import sleep
from behave import When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


A_IN_PROCESS = (By.CSS_SELECTOR, 'a.grouped-openings__locations-edit-link')
APPLICANT = (By.CSS_SELECTOR, 'a.dashboard-table__name-content.applicant-sidebar-toggle')
GO_TO_THE_NEXT_APPLICANT = (By.CSS_SELECTOR, 'button.applicant-profile-quick-actions-panel__action')
HISTORY = (By.XPATH, '/html/body/div[22]/div[2]/div[1]/div/div[4]/button[2]/span')
FILES = (By.XPATH, '/html/body/div[22]/div[2]/div[1]/div/div[4]/button[3]')
ACTIONS = (By.CSS_SELECTOR, 'body > div.applicant-sidebar > div.applicant-sidebar__content > div.applicant-sidebar__column.applicant-sidebar__column_main > div > div.applicant-profile-header > div.applicant-profile-header__actions-container.obiq-dropdown.js-obiq-dropdown.js-applicant-actions__dropdown > button')
SEND_EMAIL = (By.CSS_SELECTOR, 'div.js-send-email-modal__toggle.obiq-dropdown__item-content.js-obiq-dropdown__item-content.applicant-actions__dropdown-item-content')
SEND_TEXT = (By.CSS_SELECTOR, 'div.js-send-sms-modal__toggle.obiq-dropdown__item-content.js-obiq-dropdown__item-content.applicant-actions__dropdown-item-content')
UNSUBSCRIBE_FROM_SMS = (By.CSS_SELECTOR, 'div.js-notification-unsubscribe-confirmation-modal__toggle.obiq-dropdown__item-content.js-obiq-dropdown__item-content.applicant-actions__dropdown-item-content')
REACTIVATE_SMS = (By.CSS_SELECTOR, 'a.obiq-dropdown__item-content.js-obiq-dropdown__item-content.applicant-actions__dropdown-item-content')
REACTIVATE_EMAIL = (By.CSS_SELECTOR, 'a.obiq-dropdown__item-content.js-obiq-dropdown__item-content.applicant-actions__dropdown-item-content')
UNSUBSCRIBE_FROM_EMAIL = (By.CSS_SELECTOR, 'div.js-notification-unsubscribe-confirmation-modal__toggle.obiq-dropdown__item-content.js-obiq-dropdown__item-content.applicant-actions__dropdown-item-content')

@When('Click a in process link')
def click_link(context):
    context.driver.find_element(*A_IN_PROCESS).click()
    sleep(2)

@When('Click first applicant')
def click_applicant(context):
    context.driver.find_element(*APPLICANT).click()
    sleep(4)

@Then('Click history')
def click_history(context):
    context.driver.find_element(*HISTORY).click()
    sleep(2)

@Then('Click Files')
def click_files(context):
    context.driver.find_element(*FILES).click()
    sleep(2)

@When('Click actions')
def click_applicant_details_actions(context):
    context.driver.implicitly_wait(4)
    context.driver.find_element(*ACTIONS).click() #Click actions
    sleep(2)
@Then('Click send email')
def Send_email(context):
    context.driver.find_element(*SEND_EMAIL).click()
    sleep(4)

@Then('Send email now')
def send_email_now(context):
    context.driver.find_element_by_id('template_id').click()
    context.driver.find_element_by_css_selector('#template_id > option:nth-child(3)').click()
    sleep(1)
    context.driver.find_element_by_css_selector('button.obiq-footer-buttons__button.obiq-button.obiq-button_primary').click()
    sleep(1)

@Then('click send email later')
def send_email_later(context):
    context.driver.find_element_by_id('template_id').click()
    context.driver.find_element_by_css_selector('#template_id > option:nth-child(3)').click()
    sleep(1)
    context.driver.find_element_by_css_selector('select.obiq-form__control.obiq-form__select.obiq-select.obiq-select_full-width').click()
    context.driver.find_element_by_css_selector('#send > option:nth-child(2)').click()
    sleep(1)
    context.driver.find_element_by_css_selector('button.obiq-footer-buttons__button.obiq-button.obiq-button_primary').click()
    sleep(1)


@Then('Click Send Text/SMS now')
def send_text(context):
    context.driver.find_element(*SEND_TEXT).click()
    sleep(2)
    context.driver.find_element_by_id('template_id').click()
    sleep(1)
    context.driver.find_element_by_css_selector('#template_id > option:nth-child(2)').click()
    sleep(1)
    context.driver.find_element_by_css_selector('button.obiq-footer-buttons__button.obiq-button.obiq-button_primary').click()


@Then('Click Send Text/SMS later')
def send_text_later(context):
    context.driver.find_element(*SEND_TEXT).click()
    sleep(2)
    context.driver.find_element_by_id('template_id').click()
    sleep(1)
    context.driver.find_element_by_css_selector('#template_id > option:nth-child(2)').click()
    sleep(1)
    context.driver.find_element_by_id('send').click()
    context.driver.find_element_by_css_selector('#send > option:nth-child(2)').click()
    context.driver.find_element_by_css_selector('button.obiq-footer-buttons__button.obiq-button.obiq-button_primary').click()

@Then('Unsibscribe from SMS and reactivate SMS')
def unsibscribe_from_SMS(context):
    context.driver.find_element(*UNSUBSCRIBE_FROM_SMS).click() #clicking unsibcribe from SMS in dropdown
    context.driver.find_element_by_css_selector('button.obiq-footer-buttons__button.obiq-button.obiq-button_danger').click() #confirm
    sleep(4)
    context.driver.find_element(*ACTIONS).click() #click actions
    context.driver.find_element(*REACTIVATE_SMS).click()  #reactivate sms



@Then('Unsubscribe from Email and Reactivate Email')
def unsubscribe_from_email(context):
    context.driver.find_element(*UNSUBSCRIBE_FROM_EMAIL).click() #clicking unsibcribe from Email in dropdown
    context.driver.find_element_by_css_selector('button.obiq-footer-buttons__button.obiq-button.obiq-button_danger').click() #confirm
    sleep(4)
    context.driver.find_element(*ACTIONS).click() #click actions
    context.driver.find_element(*REACTIVATE_SMS).click()  #reactivate Email



@Then('Option to edit applicant')
def edit_applicant(context):
    context.driver.find_element_by_css_selector('body > div.obiq-dropdown__menu.js-obiq-dropdown__menu.applicant-actions__dropdown-menu.obiq-dropdown__menu_visible > div:nth-child(6) > div:nth-child(1) > a').click()
    context.driver.find_element_by_css_selector('a.obiq-footer-buttons__button.obiq-button.obiq-button_secondary.js-applicant-form__cancel-button').click()

    sleep(2)
