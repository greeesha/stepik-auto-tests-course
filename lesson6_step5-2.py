from selenium import webdriver
import time 

page = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(page)

    link = browser.find_element_by_partial_link_text(lll)
    link.click()
    
    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element('name',"last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_id('country')
    input3.send_keys("Russia")
    input4 = browser.find_element_by_class_name("city")
    input4.send_keys("Smolensk")
    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()