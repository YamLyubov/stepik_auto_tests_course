import math
import time
from selenium import webdriver as wbd

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = wbd.Chrome()
    browser.get(link)

    x_elem = browser.find_element_by_id("input_value")
    x = x_elem.text
    result = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(result)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    time.sleep(15)
    browser.quit()