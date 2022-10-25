from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 



def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
     
try: 
    
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID,"input_value").text
    
    y = calc(x)
     
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
   
    
    
    element1 = browser.find_element(By.ID, "answer")
    element1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    
    option2 = browser.find_element(By.ID, "robotsRule").click()
    
    option2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
 