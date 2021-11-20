from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/explicit_wait2.html'

with webdriver.Chrome() as browser:
    try:
        browser.get(url)
        
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        button = browser.find_element_by_id('book')
        prce = browser.find_element_by_id('price')
        WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
        button.click()
        #WebDriverWait(browser, 5).EC.element_to_be_clickable((By.ID, "verify")))
        
        xxx = browser.find_element_by_id('input_value').text
        browser.find_element_by_id('answer').send_keys(calc(xxx))

        browser.find_element_by_css_selector("[type='submit']").click()
        time.sleep(10)

    finally:
        time.sleep(10)

