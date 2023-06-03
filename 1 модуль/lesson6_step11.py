from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    
    #First name
    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.first_class .form-control.first')
    print(input1)
    input1.send_keys("Ivan")
    
    #Last name
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.second_class .form-control.second')
    print(input2)
    input2.send_keys("Petrov")

    #Email
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.third_class .form-control.third')
    print(input3)
    input3.send_keys("12345@mail.com")

    #Phone
    input4 = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.first_class .form-control.first')
    print(input4)
    input4.send_keys("88005553535")

    #Adress		
    input5 = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.second_class .form-control.second')
    print(input5)
    input5.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()


finally:

    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла