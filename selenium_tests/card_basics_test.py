import time
from test.selenium_test_case import SeleniumTestCase

class CardBasicsTest(SeleniumTestCase):
    def test_create_card(self):
        self.login_user('cardbasics%d@example.com' % time.time())
        
        # Add a new card
        self.driver.find_element_by_id('addCard').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('New Card')
        self.driver.find_element_by_id('add').click()
        
        # Go to edit page
        self.driver.find_elements_by_class_name('editCard')[0].click()
        
        # Add to key
        self.driver.find_element_by_id('addKey').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('New Key')
        score_field = self.driver.find_element_by_id('score')
        score_field.send_keys('5')
        self.driver.find_element_by_id('add').click()
        
        # Edit key
        self.driver.find_elements_by_class_name('editKey')[0].click()
        name_field = self.wait_for_id('name')
        # TODO: check contents?
        name_field.clear()
        name_field.send_keys('Updated Key')
        score_field = self.driver.find_element_by_id('score')
        score_field.clear()
        score_field.send_keys('2')
        self.driver.find_element_by_id('edit').click()
        
        # Delete key
        self.driver.find_elements_by_class_name('deleteKey')[0].click()
        self.wait_for_id('delete').click()
        
        # Add text lines
        self.driver.find_element_by_id('addText').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('First Text Line')
        self.driver.find_element_by_id('add').click()
        self.driver.find_element_by_id('addText').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Second Text Line')
        self.driver.find_element_by_id('add').click()
        
        # Move up/down
        self.driver.find_elements_by_class_name('moveUpText')[1].click()
        self.driver.find_elements_by_class_name('moveDownText')[0].click()
        
        # Edit text line
        self.driver.find_elements_by_class_name('editText')[0].click()
        name_field = self.wait_for_id('name')
        # TODO: check contents?
        name_field.clear()
        name_field.send_keys('Updated Text')
        self.driver.find_element_by_id('edit').click()
        
        # Delete text lines
        self.driver.find_elements_by_class_name('deleteText')[0].click()
        self.wait_for_id('delete').click()
        self.driver.find_elements_by_class_name('deleteText')[0].click()
        self.wait_for_id('delete').click()
        
        time.sleep(3)
        