from time import sleep

from selenium import webdriver
from selenium.webdriver.common import by



#init driver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('drivers/chromedriver')


driver.get('https://www.google.com')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('dress')

sleep(4)

driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()