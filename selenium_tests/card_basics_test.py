import time
from test.selenium_test_case import SeleniumTestCase

class CardBasicsTest(SeleniumTestCase):
    def test_create_card(self):
        self.login_user('cardbasics@example.com')
        
        add_button = self.driver.find_element_by_id('addCard')
        add_button.click()
        
        name_field = self.wait_for_id('name')
        name_field.clear()
        name_field.send_keys('New Card %d' % time.time())
        save_button = self.driver.find_element_by_id('add')
        save_button.click()