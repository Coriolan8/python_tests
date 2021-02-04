from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input4 = browser.find_element_by_id("answer")
    input4.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    #browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer) #скрывает ненужный элемент footer
    radio.click()
    submit = browser.find_element_by_xpath("//button[text()= 'Submit']")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

