from selenium import webdriver
from selenium.webdriver.common.by import By

import time, math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
	
    button_1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    print(input)
    input.send_keys(y)

    button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:

    time.sleep(30)
    browser.quit()

