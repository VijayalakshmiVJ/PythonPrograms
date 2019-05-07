# using chrome and selenium to login into google mail

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://mail.google.com/mail')

#emailElem = browser.find_element_by_id('login-username')
emailElem = browser.find_element_by_name('identifier')
emailElem.send_keys('vijayalakshmi.halwar')
elem = browser.find_element_by_xpath("//*[@id='identifierNext']/content/span")
elem.click()

#passwordElem = browser.find_element_by_name('password')
#passwordElem = browser.find_element_by_class_name('whsOnd zHQkBf')
#passwordElem = browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
#passwordElem = browser.find_element_by_id('password')
#passwordElem = browser.find_element_by_xpath('//input[@name="password"]')

browser.implicitly_wait(10)

passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys()
elem = browser.find_element_by_xpath("//*[@id='passwordNext']/content/span")
elem.click()


