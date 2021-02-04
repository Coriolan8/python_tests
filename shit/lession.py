from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    element1 = browser.find_element_by_xpath("//div[@class='first_block']/div[1]/input")
    element1.send_keys("1")
    element2 = browser.find_element_by_xpath("//div[@class='first_block']/div[2]/input")
    element2.send_keys("2")
    element2 = browser.find_element_by_xpath("//div[@class='first_block']/div[3]/input")
    element2.send_keys("3")
    element3 = browser.find_element_by_xpath("//div[@class='second_block']/div[1]/input")
    element3.send_keys("1")
    element4 = browser.find_element_by_xpath("//div[@class='second_block']/div[2]/input")
    element4.send_keys("2")
        
   
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
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

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
