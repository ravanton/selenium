from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
     
try: 
    
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID,"input_value").text
    
    y = calc(x)
     
    
   
    
    
    element1 = browser.find_element(By.ID, "answer")
    element1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    option2.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()