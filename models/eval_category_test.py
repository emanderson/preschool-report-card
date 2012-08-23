import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from eval_category import EvalCategory
from eval_item import EvalItem
from report_card import ReportCard

class EvalCategoryTest(ModelTestCase):
    def setUp(self):
        super(EvalCategoryTest, self).setUp()
        self.card_id = ReportCard.create('Category Test Card').id()
    
    def test_create(self):
        category_id = EvalCategory.create('Category Create Test', self.card_id).id()
        category = EvalCategory.find_by_id(category_id)
        self.assertEqual('Category Create Test', category.name)
        self.assertEqual(self.card_id, category.card.key().id())

    def test_items(self):
        category_id = EvalCategory.create('Category Items Test', self.card_id).id()
        item1 = EvalItem.find_by_id(EvalItem.create('Category Items Test 1', category_id).id())
        item1.position = 5
        item1.put()
        item2 = EvalItem.find_by_id(EvalItem.create('Category Items Test 2', category_id).id())
        item2.position = 2
        item2.put()
        item3 = EvalItem.find_by_id(EvalItem.create('Category Items Test 3', category_id).id())
        items = EvalCategory.find_by_id(category_id).items()
        self.assertEqual(3, len(items))
        self.assertEqual('Category Items Test 2', items[0].name)
        self.assertEqual('Category Items Test 1', items[1].name)
        self.assertEqual('Category Items Test 3', items[2].name)