from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration1.html"

with webdriver.Chrome() as browser:

    browser.get(link)
    #elements = browser.find_elements_by_tag_name ("input")
    elements = browser.find_elements_by_css_selector("input[required]")
    for element in elements:
        element.send_keys("Мой ответ")


    button = browser.find_element_by_tag_name("button")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
    #for i in range(len(elements)):
       #browser.execute_script(f'document.getElementsByTagName("input")[{i}].value = "Мой ответ"')
