import time
from test.selenium_test_case import SeleniumTestCase

class CardBasicsTest(SeleniumTestCase):
    def test_edit_card(self):
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
        self.wait_for_removal('mask')
        
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
        
        # Add text lines
        self.driver.find_element_by_id('addText').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('First Text Line')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        self.driver.find_element_by_id('addText').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Second Text Line')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        
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
        
        # Add categories
        self.driver.find_element_by_id('addCategory').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('First Category')
        self.driver.find_element_by_id('add').click()
        self.driver.find_element_by_id('addCategory').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Second Category')
        self.driver.find_element_by_id('add').click()
        
        # Move categories up/down
        self.driver.find_elements_by_class_name('moveUpCategory')[1].click()
        self.driver.find_elements_by_class_name('moveDownCategory')[0].click()
        
        # Edit category
        self.driver.find_elements_by_class_name('editCategory')[0].click()
        name_field = self.wait_for_id('name')
        # TODO: check contents?
        name_field.clear()
        name_field.send_keys('Updated Category')
        self.driver.find_element_by_id('edit').click()
        
        # Add items
        self.driver.find_elements_by_class_name('addEvalItem')[0].click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('First Item')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        self.driver.find_elements_by_class_name('addEvalItem')[0].click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Second Item')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        
        # Move items up/down
        self.driver.find_elements_by_class_name('moveUpItem')[1].click()
        self.driver.find_elements_by_class_name('moveDownItem')[0].click()
        
        # Edit item
        self.driver.find_elements_by_class_name('editItem')[0].click()
        name_field = self.wait_for_id('name')
        # TODO: check contents?
        name_field.clear()
        name_field.send_keys('Updated Item')
        self.driver.find_element_by_id('edit').click()
        
        # Add signatures
        self.driver.find_element_by_id('addSignature').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('First Signature')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        self.driver.find_element_by_id('addSignature').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Second Signature')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        
        # Move signatures up/down
        self.driver.find_elements_by_class_name('moveUpSignature')[1].click()
        self.driver.find_elements_by_class_name('moveDownSignature')[0].click()
        
        # Edit signature
        self.driver.find_elements_by_class_name('editSignature')[0].click()
        name_field = self.wait_for_id('name')
        # TODO: check contents?
        name_field.clear()
        name_field.send_keys('Updated Signature')
        self.driver.find_element_by_id('edit').click()
        
        # Preview
        self.driver.find_element_by_id('previewButton').click()
        
        # Back to Edit
        self.driver.find_element_by_id('editButton').click()
        
        # Delete key
        self.driver.find_elements_by_class_name('deleteKey')[0].click()
        self.wait_for_id('delete').click()
        
        # Delete text lines
        self.driver.find_elements_by_class_name('deleteText')[0].click()
        self.wait_for_id('delete').click()
        self.driver.find_elements_by_class_name('deleteText')[0].click()
        self.wait_for_id('delete').click()
        
        # Delete item
        self.driver.find_elements_by_class_name('deleteItem')[0].click()
        self.wait_for_id('delete').click()
        
        # Delete categories
        self.driver.find_elements_by_class_name('deleteCategory')[0].click()
        self.wait_for_id('delete').click()
        self.driver.find_elements_by_class_name('deleteCategory')[0].click()
        self.wait_for_id('delete').click()
        
        # Delete signatures
        self.driver.find_elements_by_class_name('deleteSignature')[0].click()
        self.wait_for_id('delete').click()
        self.driver.find_elements_by_class_name('deleteSignature')[0].click()
        self.wait_for_id('delete').click()

    def test_fill_card(self):
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
        self.wait_for_removal('mask')
        
        # Add text lines
        self.driver.find_element_by_id('addText').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('First Text Line')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        self.driver.find_element_by_id('addText').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Second Text Line')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        
        # Add categories
        self.driver.find_element_by_id('addCategory').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('First Category')
        self.driver.find_element_by_id('add').click()
        self.driver.find_element_by_id('addCategory').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Second Category')
        self.driver.find_element_by_id('add').click()
        
        # Add items
        self.driver.find_elements_by_class_name('addEvalItem')[0].click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('First Item')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        self.driver.find_elements_by_class_name('addEvalItem')[0].click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Second Item')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        self.driver.find_elements_by_class_name('addEvalItem')[1].click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Third Item')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        
        # Add signatures
        self.driver.find_element_by_id('addSignature').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('First Signature')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        self.driver.find_element_by_id('addSignature').click()
        name_field = self.wait_for_id('name')
        name_field.send_keys('Second Signature')
        self.driver.find_element_by_id('add').click()
        self.wait_for_removal('mask')
        
        # Back to card list and to fill page
        self.driver.find_element_by_id("cardList").click()
        self.driver.find_elements_by_class_name("fillCard")[0].click()
        
        # Add a student
        self.driver.find_element_by_id("addFill").click()
        name_field = self.wait_for_id('name')
        name_field.send_keys("Student")
        self.driver.find_element_by_id('add').click()
        
        # Fill out for that student
        self.driver.find_elements_by_class_name('fillOut')[0].click()
        text_lines = self.driver.find_elements_by_class_name('textValue')
        for line in text_lines:
            line.send_keys('Some Text for a Line')
        item_scores = self.driver.find_elements_by_class_name('itemScore')
        for score in item_scores:
            score.send_keys('5')
        self.driver.find_element_by_id('comments').send_keys('Some interesting comments')
        self.driver.find_element_by_id('save').click()
        