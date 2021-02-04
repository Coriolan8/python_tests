from selenium import webdriver
import time
import  os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    name.send_keys("Ivan")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("dfds")
    email = browser.find_element_by_name("email")
    email.send_keys("ds@fg.c")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '../file.txt')           # добавляем к этому пути имя файла
    browser.find_element_by_name('file').send_keys(file_path)
    submit = browser.find_element_by_xpath("//button[text()= 'Submit']")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()