
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

browser.get('http://inventwithpython.com')
