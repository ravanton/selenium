from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 



def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
     
try: 
    
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID,"input_value").text
    
    y = calc(x)
     
    
   
    
    
    element1 = browser.find_element(By.ID, "answer")
    element1.send_keys(y)
    
    option = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
 