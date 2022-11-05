from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest
from selenium.common.exceptions import NoSuchElementException


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link1)
browser.get(link2)  


class Link:
    def __init__ (self, link):
        browser.get(link)


    # Ваш код, который заполняет обязательные поля
    def find_and_click(self):
        
        browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']").send_keys("Yep")
        browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']").send_keys("Yep")
        browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']").send_keys("Yep")
        browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control first']").send_keys("123")
        browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control second']").send_keys("yep")
        browser.find_element_by_class_name('btn').click()


    def get_answer(self):
        return(browser.find_element_by_tag_name("h1").text)


    def close(self):
        browser.quit()

class TestUrl(unittest.TestCase):
    def test_link1(self):
        link = Link(link1)
        link.find_and_click()
        self.assertEqual(link.get_answer(), "Congratulations! You have successfully registered!", 'Error Registration 1')
   
    def test_link2(self):
        link = Link(link2)
        link.find_and_click()
        self.assertEqual(link.get_answer(), "Congratulations! You have successfully registered!", 'Error Registration 2')
   

if __name__ == "__main__":
    unittest.main()
 