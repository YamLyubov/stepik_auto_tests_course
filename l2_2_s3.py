import time
from selenium import webdriver as wbd
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = wbd.Chrome()
    browser.get(link)

    x_elem = browser.find_element_by_id('num1')
    x = int(x_elem.text)

    y_elem = browser.find_element_by_id('num2')
    y = int(y_elem.text)
    result = x + y

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(result))

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    time.sleep(15)
    browser.quit()

