from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://stepik.org/lesson/236895/step/1?auth=login"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.ID, "id_login_email")
input1.send_keys("antonrekhva@gmail.com")
input2 = browser.find_element(By.NAME, "id_login_password")
input2.send_keys("vocmo3-Kejjom-hazfyv")
  
button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn ")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()