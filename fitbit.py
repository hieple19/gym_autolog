import config # 2 variables: user (email) and pw (password)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
wait = WebDriverWait(browser, 20)

browser.get('https://fitbit.com')
browser.find_element_by_link_text('Log in').click()

price = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ember644")))
user = browser.find_element_by_id('ember644')
user.send_keys(config.user)
pw = browser.find_element_by_id('ember645')
pw.send_keys(config.pw)
pw.submit()

price = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".dashHeader")))

browser.find_element_by_link_text('Log').click()
browser.find_element_by_link_text('Activities').click()

browser.find_element_by_class_name('open-annotation-form').click()

browser.find_element_by_css_selector('.field .entry input').send_keys('hiep')

browser.execute_script("document.querySelector('.field.date input').value = '2019-12-12'");

browser.find_element_by_css_selector('.time-fields input').send_keys('1150')
browser.find_element_by_css_selector('.end-time input').send_keys('1350')

browser.find_element_by_css_selector('.end-time input').submit()