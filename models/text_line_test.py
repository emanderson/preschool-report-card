import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from text_line import TextLine
from report_card import ReportCard

class TextLineTest(ModelTestCase):
    def setUp(self):
        super(TextLineTest, self).setUp()
        self.card_id = ReportCard.create('Text Line Test Card').id()
    
    def test_create(self):
        text_line_id = TextLine.create('Text Line Create Test', self.card_id).id()
        text_line = TextLine.find_by_id(text_line_id)
        self.assertEqual('Text Line Create Test', text_line.name)
        self.assertEqual(self.card_id, text_line.card.key().id())