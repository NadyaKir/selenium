from selenium import webdriver
from selenium.webdriver.common.by import By

import time, math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    print(input)
    input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
    radioButton = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:

    time.sleep(30)
    browser.quit()

