'''Chrome testing with selenium requires a chromedriver from 
https://code.google.com/p/chromedriver/downloads/list to be installed and in the PATH'''

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class SeleniumTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def tearDown(self):
        self.driver.quit()
    
    def login_user(self, email):
        # This assumes no user is already logged in
        self.driver.get('http://0.0.0.0:8083')
        login_email = self.driver.find_element_by_id('email')
        login_email.clear()
        login_email.send_keys(email)
        login_button = self.driver.find_element_by_id('submit-login')
        login_button.click()
    
    def wait_for_id(self, id, max_wait=10):
        return WebDriverWait(self.driver, max_wait).until(lambda driver: driver.find_element_by_id(id))
    
    def wait_for_removal(self, class_name, max_wait=10):
        return WebDriverWait(self.driver, max_wait).until(lambda driver: len(driver.find_elements_by_class_name(class_name)) == 0)
    