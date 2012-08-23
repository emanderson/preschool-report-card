import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from eval_category import EvalCategory
from eval_item import EvalItem
from eval_item_data import EvalItemData
from comment_data import CommentData
from report_card import ReportCard
from evaluation import Evaluation
from text_line import TextLine
from text_line_data import TextLineData

class EvalCategoryTest(ModelTestCase):
    def setUp(self):
        super(EvalCategoryTest, self).setUp()
        self.card_id = ReportCard.create('Evaluation Test Card').id()
        self.category1_id = EvalCategory.create('Evaluation Test Category 1', self.card_id).id()
        self.category2_id = EvalCategory.create('Evaluation Test Category 2', self.card_id).id()
        self.item1_id = EvalItem.create('Evaluation Test Item 1', self.category1_id).id()
        self.item2_id = EvalItem.create('Evaluation Test Item 2', self.category1_id).id()
        self.item3_id = EvalItem.create('Evaluation Test Item 3', self.category2_id).id()
        self.text_line1_id = TextLine.create('Evaluation Test Text Line 1', self.card_id).id()
        self.text_line2_id = TextLine.create('Evaluation Test Text Line 2', self.card_id).id()
    
    def test_create(self):
        eval_id = Evaluation.create('Evaluation Create Test', self.card_id).id()
        evaluation = Evaluation.find_by_id(eval_id)
        self.assertEqual('Evaluation Create Test', evaluation.name)
        self.assertEqual(self.card_id, evaluation.card.key().id())

    def test_all_data(self):
        eval_id = Evaluation.create('Evaluation Create Test', self.card_id).id()
        EvalItemData.create_or_update(self.item1_id, eval_id, 'Item 1 Value')
        EvalItemData.create_or_update(self.item2_id, eval_id, 'Item 2 Value')
        CommentData.create_or_update(eval_id, 'Comments')
        TextLineData.create_or_update(self.text_line1_id, eval_id, 'Text Line 1 Value')
        all_data = Evaluation.find_by_id(eval_id).all_data()
        self.assertEqual('Item 1 Value', all_data['items'][self.item1_id])
        self.assertEqual('Item 2 Value', all_data['items'][self.item2_id])
        self.assertEqual('', all_data['items'][self.item3_id])
        self.assertEqual('Comments', all_data['comments'])
        self.assertEqual('Text Line 1 Value', all_data['text'][self.text_line1_id])
        self.assertEqual('', all_data['text'][self.text_line2_id])