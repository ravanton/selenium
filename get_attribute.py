from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
     
try: 
    
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,"treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
     
    
   
    
    
    element1 = browser.find_element(By.ID, "answer")
    element1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option1.click()
    option2 = browser.find_element(By.ID, "robotCheckbox")
    option2.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    option2.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()