from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    try:
        browser.get(link)

        element = browser.find_element_by_id('input_value')
        xxx = element.text
        yyy = calc(xxx)
        
        browser.find_element_by_id('answer').send_keys(yyy)
        
        option1 = browser.find_element_by_id('robotCheckbox')
        option1.click()
        
        option2 = browser.find_element_by_css_selector("[for='robotsRule']")
        option2.click()

        button = browser.find_element_by_tag_name("button")
        button.click()
        time.sleep(10)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        time.sleep(1)

