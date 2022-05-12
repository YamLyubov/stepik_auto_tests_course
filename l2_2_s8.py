import time
import os
from selenium import webdriver as wbd

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = wbd.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys('text')

    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys('text')

    email = browser.find_element_by_name("email")
    email.send_keys('text')

    email = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')  # добавляем к этому пути имя файла
    email.send_keys(file_path)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    time.sleep(15)
    browser.quit()