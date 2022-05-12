import math
import time
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = wbd.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element_by_id('book')
    button.click()

    x_elem = browser.find_element_by_id("input_value")
    x = x_elem.text
    result = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(result)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
finally:
    time.sleep(20)
    browser.quit()