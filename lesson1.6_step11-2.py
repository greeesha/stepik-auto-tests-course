from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        
        # вот правильный вариант, для нормальной вёрстки, но не выполняющий плохо написанные условия ТЗ на этот тест (см. камменты)
        
        #elements = browser.find_elements_by_css_selector("input[required]")
        #for element in elements:
        #    element.send_keys("Мой ответ")
        
        # а вот какая- то фигня, выполняющая, то что хотел преподаватель.

        element = browser.find_element_by_xpath('//div[@class="first_block"]/div[contains(@class, "first_class")]/input[contains(@class, "first")]')
        element.send_keys("Мой ответ")
        element = browser.find_element_by_xpath('//div[@class="first_block"]/div[contains(@class, "second_class")]/input[contains(@class, "second")]')
        element.send_keys("Мой ответ")
        element = browser.find_element_by_xpath('//div[@class="first_block"]/div[contains(@class, "third_class")]/input[contains(@class, "third")]')
        element.send_keys("Мой ответ")

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

