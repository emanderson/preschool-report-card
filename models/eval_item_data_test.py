import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from evaluation import Evaluation
from eval_category import EvalCategory
from eval_item import EvalItem
from eval_item_data import EvalItemData
from report_card import ReportCard
from comment_data import CommentData

class EvalItemDataTest(ModelTestCase):
    def setUp(self):
        super(EvalItemDataTest, self).setUp()
        self.card_id = ReportCard.create('Item Data Test Card').id()
        self.evaluation_id = Evaluation.create('Item Data Test Evaluation', self.card_id).id()
        self.category_id = EvalCategory.create('Item Data Test Category', self.card_id).id()
        self.item_id = EvalItem.create('Item Data Test Item', self.category_id).id()

    def test_create_or_update(self):
        first_id = EvalItemData.create_or_update(self.item_id, self.evaluation_id, 'Item Data Test Value').id()
        second_id = EvalItemData.create_or_update(self.item_id, self.evaluation_id, 'Item Data Test New Value').id()
        self.assertEqual(first_id, second_id)
        item_data = EvalItemData.find_by_id(second_id)
        self.assertEqual('Item Data Test New Value', item_data.value)