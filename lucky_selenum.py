
import sys, webbrowser
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))


#linkElems = browser.find_elements_by_class_name('r')
linkElems = browser.find_elements_by_css_selector('.r a')
#linkElems = browser.find_elements_by_xpath('//a[@href]')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get_attribute('href'))
