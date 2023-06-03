from selenium import webdriver
from selenium.webdriver.common.by import By

import time, math

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 100);")

    x = browser.find_element(By.ID, 'input_value').text
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

