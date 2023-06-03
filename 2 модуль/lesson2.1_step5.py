from selenium import webdriver
from selenium.webdriver.common.by import By

import time, math

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    print(input)
    input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
    radioButton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:

    time.sleep(30)
    browser.quit()

