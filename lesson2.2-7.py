from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"
fname = 'try.txt'

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, fname)           # добавляем к этому пути имя файла 

#Возможно кому-то будет полезно) Что бы ручками не создавать файл, можно сделать это с помощью python.
#with open("test.txt", "w") as file:
#    content = file.write("automationbypython")  # create test.txt file

with webdriver.Chrome() as browser:
    try:
        browser.get(link)

        browser.find_element_by_name('firstname').send_keys('Имя')
        browser.find_element_by_name('lastname').send_keys('Фамилия')
        browser.find_element_by_name('email').send_keys('Email@Email.com')
        browser.find_element_by_name('file').send_keys(file_path)



        button = browser.find_element_by_tag_name("button")
        button.click()
        time.sleep(10)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        time.sleep(1)

