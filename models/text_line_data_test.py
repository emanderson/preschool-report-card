import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from evaluation import Evaluation
from text_line import TextLine
from text_line_data import TextLineData
from report_card import ReportCard

class TextLineDataTest(ModelTestCase):
    def setUp(self):
        super(TextLineDataTest, self).setUp()
        self.card_id = ReportCard.create('Text Line Data Test Card').id()
        self.evaluation_id = Evaluation.create('Text Line Data Test Evaluation', self.card_id).id()
        self.text_line_id = TextLine.create('Text Line Data Test Text Line', self.card_id).id()

    def test_create_or_update(self):
        first_id = TextLineData.create_or_update(self.text_line_id, self.evaluation_id, 'Text Line Data Test Value').id()
        second_id = TextLineData.create_or_update(self.text_line_id, self.evaluation_id, 'Text Line Data Test New Value').id()
        self.assertEqual(first_id, second_id)
        text_line_data = TextLineData.find_by_id(second_id)
        self.assertEqual('Text Line Data Test New Value', text_line_data.value)