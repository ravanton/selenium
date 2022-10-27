from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    # Ваш код, который заполняет обязательные поля
    elements = browser.find_elements(By.CSS_SELECTOR, ".form-group input[required] ")
    for element in elements:
        element.send_keys("Yep") 

    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    # имя файла, который будем загружать на сайт
    file_name = "file.txt"
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, "file.txt")  
    # находим кнопку отправить файл, имеет атрибут type="file"        
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # отправляем файл
    element.send_keys(file_path)
     
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
 