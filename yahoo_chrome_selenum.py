
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://mail.yahoo.com')

#emailElem = browser.find_element_by_id('login-username')
emailElem = browser.find_element_by_name('username')
emailElem.send_keys('not_my_real_email')
