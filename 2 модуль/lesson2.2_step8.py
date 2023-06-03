from selenium import webdriver
from selenium.webdriver.common.by import By

import time, math, os

link = "http://suninjuly.github.io/file_input.html"

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
	
    #First name
    input1 = browser.find_element(By.NAME, 'firstname')
    print(input1)
    input1.send_keys('Nadya')

    #Last name
    input2 = browser.find_element(By.NAME, 'lastname')
    print(input2)
    input2.send_keys('Kireyeva')

    #Email
    input3 = browser.find_element(By.NAME, 'email')
    print(input3)
    input3.send_keys('12345@mail.com')

    #File
    current_dir = os.path.abspath(os.path.dirname(__file__))   
    file_path = os.path.join(current_dir, 'file.txt')

    input4 = browser.find_element(By.ID, 'file')
    print(input4)           
    input4.send_keys(file_path)


    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


finally:

    time.sleep(30)
    browser.quit()

