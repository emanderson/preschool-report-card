import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from eval_key_level import EvalKeyLevel
from report_card import ReportCard

class EvalKeyLevelTest(ModelTestCase):
    def setUp(self):
        super(EvalKeyLevelTest, self).setUp()
        self.card_id = ReportCard.create('Eval Key Level Test Card').id()
    
    def test_create(self):
        eval_key_level_id = EvalKeyLevel.create('Eval Key Level Test', 5, self.card_id).id()
        eval_key_level = EvalKeyLevel.find_by_id(eval_key_level_id)
        self.assertEqual('Eval Key Level Test', eval_key_level.name)
        self.assertEqual(self.card_id, eval_key_level.card.key().id())