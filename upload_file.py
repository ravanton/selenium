from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 
import os 



     
try: 
    
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    # Ваш код, который заполняет обязательные поля
    elements = browser.find_elements(By.CSS_SELECTOR, ".form-group input[required] ")
    for element in elements:
        element.send_keys("Hi") 

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)
     
    
   
    
    
    input1 = browser.find_element(By.ID, "answer")
    

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    
    option2 = browser.find_element(By.ID, "robotsRule").click()
    
    option2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
 