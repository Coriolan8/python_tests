from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = " http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_id("num1").text
    b = browser.find_element_by_id("num2").text

    Select = Select(browser.find_element_by_id('dropdown'))
    Select.select_by_value(str(int(a)+int(b)))
    submit = browser.find_element_by_xpath("//button[text()= 'Submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
