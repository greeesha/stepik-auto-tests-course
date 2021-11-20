from selenium import webdriver
import time 

link = "http://suninjuly.github.io/huge_form.html"

with webdriver.Chrome() as browser:

    browser.get(link)
    #elements = browser.find_elements_by_tag_name ("input")
    elements = browser.find_elements_by_css_selector("input[type='text']")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(30)
    
    #for i in range(len(elements)):
       #browser.execute_script(f'document.getElementsByTagName("input")[{i}].value = "Мой ответ"')
