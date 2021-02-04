from selenium import webdriver
import time
import math


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    button = browser.find_element_by_tag_name("button").click()
    new_window = browser.window_handles[1]  # Переключение на новою вкладку
    browser.switch_to.window(new_window)  # Активация новой вкладки
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text # ЗАбирает текст атрибута
    y = calc(x)   # Запускает функцию calc
    input4 = browser.find_element_by_id("answer")
    input4.send_keys(y)
    submit = browser.find_element_by_xpath("//button[text()= 'Submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()