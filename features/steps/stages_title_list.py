from behave import When, then
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from time import sleep

LINK_FIRST_CLICK = (By.CSS_SELECTOR, 'a.grouped-openings__locations-edit-link')

@When('Click applicants in process link')
def click_link(context):
    context.driver.find_element(*LINK_FIRST_CLICK).click()
    sleep(3)


@When('Click carousel')
def select_carousel(context):
    expected_titles = ['Landing', 'In-person Interview', 'Background Check', 'Document upload', 'Approved', 'Rejected',
                       'On Hold']
    context.driver.implicitly_wait(2)
    carousel = context.driver.find_element_by_css_selector('div.js-stages-carousel')
    carousel = carousel.find_element_by_css_selector('div.stages-carousel')
    carousel = carousel.find_element_by_css_selector("div.stages-carousel__item-group.swiper-slide-active")
    carousel_items = carousel.find_elements_by_css_selector("a.stages-carousel__item")

    for expected_title, box in zip(expected_titles, carousel_items):
        actual_title = box.find_element_by_css_selector("span.stages-carousel__item-title").text
        assert actual_title == expected_title, "Expected title {}, but got {}".format(expected_title, actual_title)






@then('Verify user can select through stages')
def verify_title_selection(context):
    expected_titles = ['Landing', 'In-person Interview', 'Background Check', 'Document upload', 'Approved', 'Rejected', 'On Hold']
    title_webelements = context.driver.find_elements(*LINKS_CAR)
    print('\n\nWebElements:\n', title_webelements)

    for title_webelement in title_webelements:
        if len(title_webelement.text) == 0:
            print('\n', len(title_webelement.text))
            context.driver.find_element(*NEXT_BTN).click()
        print('\n\nWebElement:\n', title_webelement.text)
        assert title_webelement.text == expected_titles[title_webelements.index(title_webelement)]

