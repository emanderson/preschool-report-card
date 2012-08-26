from test.handler_test_case import HandlerTestCase

from category_handler import CategoryHandler
from models.report_card import ReportCard
from models.text_line import TextLine

class TextLineHandlerTest(HandlerTestCase):
    def setUp(self):
        super(TextLineHandlerTest, self).setUp()
        self.card_id = ReportCard.create(name='Category Test Card').id()

    def test_add_form(self):
        response = self.testapp.get('/card/%d/text_line/add_form' % self.card_id)
        self.assertSuccess(response)
    
    def test_add(self):
        response = self.testapp.get('/card/%d/text_line/add' % self.card_id, {'name': 'Add Test Name'})
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(1, len(card.text_lines()))
        self.assertEqual('Add Test Name', card.text_lines()[0].name)
    
    def test_edit_form(self):
        text_line_id = TextLine.create('Edit Form Test Name', self.card_id).id()
        response = self.testapp.get('/text_line/%d/edit_form' % text_line_id)
        self.assertSuccess(response)
    
    def test_edit(self):
        text_line_id = TextLine.create('Edit Test Name', self.card_id).id()
        response = self.testapp.post('/text_line/%d/edit' % text_line_id, {'name': 'Edit Test New Name'})
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(1, len(card.text_lines()))
        self.assertEqual('Edit Test New Name', card.text_lines()[0].name)
    
    def test_delete_form(self):
        text_line_id = TextLine.create('Delete Form Test Name', self.card_id).id()
        response = self.testapp.get('/text_line/%d/delete_form' % text_line_id)
        self.assertSuccess(response)
    
    def test_delete(self):
        text_line_id = TextLine.create('Delete Test Name', self.card_id).id()
        response = self.testapp.post('/text_line/%d/delete' % text_line_id)
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(0, len(card.text_lines()))
    
    def test_move_up(self):
        text_line1_id = TextLine.create('Move Up Test Name 1', self.card_id).id()
        text_line2_id = TextLine.create('Move Up Test Name 2', self.card_id).id()
        response = self.testapp.post('/text_line/%d/move_up' % text_line2_id)
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        text_lines = card.text_lines()
        self.assertEqual(2, len(text_lines))
        self.assertEqual(text_line2_id, text_lines[0].key().id())
        self.assertEqual(text_line1_id, text_lines[1].key().id())
    
    def test_move_down(self):
        text_line1_id = TextLine.create('Move Up Test Name 1', self.card_id).id()
        text_line2_id = TextLine.create('Move Up Test Name 2', self.card_id).id()
        response = self.testapp.post('/text_line/%d/move_down' % text_line1_id)
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        text_lines = card.text_lines()
        self.assertEqual(2, len(text_lines))
        self.assertEqual(text_line2_id, text_lines[0].key().id())
        self.assertEqual(text_line1_id, text_lines[1].key().id())
        