import time
from selenium import webdriver as wbd
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = wbd.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_elem = browser.find_element_by_id("input_value")
    x = x_elem.text
    result = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(result)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    time.sleep(15)
    browser.quit()