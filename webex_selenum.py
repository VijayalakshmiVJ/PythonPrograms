from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

#browser.get('https://nokiameetings.webex.com/mw3100/mywebex/default.do?siteurl=nokiameetings&rnd=0.8793165685131364')
browser.get('https://mail.yahoo.com')

try:
    print('testing')
    #elem = browser.find_element_by_id('mc-ipt-meetingNum')
    elem = browser.find_element_by_id('login-username')
    
    #elem.click()
    print('Found <%s> element with that class name!' % (elem.tag_name))
    elem.send_keys('test')
    elem.submit()
except:
    print('Was not able to find an element with that name.')
