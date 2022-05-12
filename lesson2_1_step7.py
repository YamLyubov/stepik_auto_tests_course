import math
import time
from selenium import webdriver as wbd


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = wbd.Chrome()
    browser.get(link)

    img = browser.find_element_by_id("treasure")
    x = img.get_attribute('valuex')
    result = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(result)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
