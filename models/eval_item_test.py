import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from eval_category import EvalCategory
from eval_item import EvalItem
from report_card import ReportCard

class EvalItemTest(ModelTestCase):
    def setUp(self):
        super(EvalItemTest, self).setUp()
        self.card_id = ReportCard.create('Item Test Card').id()
        self.category_id = EvalCategory.create('Item Test Category', self.card_id).id()
    
    def test_create(self):
        item_id = EvalItem.create('Item Create Test', self.category_id).id()
        item = EvalItem.find_by_id(item_id)
        self.assertEqual('Item Create Test', item.name)
        self.assertEqual(self.category_id, item.category.key().id())