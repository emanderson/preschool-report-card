import time
from test.selenium_test_case import SeleniumTestCase

class CardBasicsTest(SeleniumTestCase):
    def test_create_card(self):
        self.login_user('cardbasics%d@example.com' % time.time())
        
        # Add a new card
        add_button = self.driver.find_element_by_id('addCard')
        add_button.click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('New Card')
        save_button = self.driver.find_element_by_id('add')
        save_button.click()
        
        # Go to edit page
        edit_button = self.driver.find_elements_by_class_name('editCard')[0]
        edit_button.click()
        
        # Add to key
        add_key_button = self.driver.find_element_by_id('addKey')
        add_key_button.click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('New Key')
        score_field = self.driver.find_element_by_id('score')
        score_field.send_keys('5')
        save_button = self.driver.find_element_by_id('add')
        save_button.click()
        
        # Edit key
        edit_key_button = self.driver.find_elements_by_class_name('editKey')[0]
        edit_key_button.click()
        name_field = self.wait_for_id('name')
        # TODO: check contents?
        name_field.clear()
        name_field.send_keys('Updated Key')
        score_field = self.driver.find_element_by_id('score')
        score_field.clear()
        score_field.send_keys('2')
        save_button = self.driver.find_element_by_id('edit')
        save_button.click()
        
        # Delete key
        delete_key_button = self.driver.find_elements_by_class_name('deleteKey')[0]
        delete_key_button.click()
        delete_button = self.wait_for_id('delete')
        delete_button.click()
        
        # Add text line
        add_text_button = self.driver.find_element_by_id('addText')
        add_text_button.click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('New Text Line')
        save_button = self.driver.find_element_by_id('add')
        save_button.click()
        
        # Edit text line
        edit_text_button = self.driver.find_elements_by_class_name('editText')[0]
        edit_text_button.click()
        name_field = self.wait_for_id('name')
        # TODO: check contents?
        name_field.clear()
        name_field.send_keys('Updated Text')
        save_button = self.driver.find_element_by_id('edit')
        save_button.click()
        
        # Delete text line
        delete_text_button = self.driver.find_elements_by_class_name('deleteText')[0]
        delete_text_button.click()
        delete_button = self.wait_for_id('delete')
        delete_button.click()
        
        time.sleep(3)
        