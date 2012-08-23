import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from evaluation import Evaluation
from eval_category import EvalCategory
from eval_item import EvalItem
from app_user import AppUser
from eval_key_level import EvalKeyLevel
from signature import Signature
from text_line import TextLine
from report_card import ReportCard

class ReportCardTest(ModelTestCase):
    def test_create(self):
        card_id = ReportCard.create('Report Card Create Test').id()
        card = ReportCard.find_by_id(card_id)
        self.assertEqual('Report Card Create Test', card.name)
        self.assertEqual(users.get_current_user().user_id(), card.owner_user_id[0])
    
    def test_list_by_user(self):
        card_id = ReportCard.create('Report Card List By User Test').id()
        cards = ReportCard.list_by_user()
        self.assertEqual(1, len(cards))
        self.assertEqual(card_id, cards[0].key().id())
        
        card = ReportCard.find_by_id(card_id)
        card.owner_user_id = []
        card.put()
        cards = ReportCard.list_by_user()
        self.assertEqual(0, len(cards))
        
        self.makeAdmin()
        cards = ReportCard.list_by_user()
        self.assertEqual(1, len(cards))
        self.assertEqual(card_id, cards[0].key().id())
    
    def test_is_authorized(self):
        card_id = ReportCard.create('Report Card Is Authorized Test').id()
        card = ReportCard.find_by_id(card_id)
        self.assertTrue(card.is_authorized())
        
        card.owner_user_id = []
        card.put()
        card = ReportCard.find_by_id(card_id)
        self.assertFalse(card.is_authorized())
        
        self.makeAdmin()
        card = ReportCard.find_by_id(card_id)
        self.assertTrue(card.is_authorized())

    def test_categories(self):
        card_id = ReportCard.create('Report Card Categories Test').id()
        category1 = EvalCategory.find_by_id(EvalCategory.create('Report Card Categories Test 1', card_id).id())
        category1.position = 4
        category1.put()
        category2 = EvalCategory.find_by_id(EvalCategory.create('Report Card Categories Test 2', card_id).id())
        category2.position = 1
        category2.put()
        category3 = EvalCategory.find_by_id(EvalCategory.create('Report Card Categories Test 3', card_id).id())
        categories = ReportCard.find_by_id(card_id).categories()
        self.assertEqual(3, len(categories))
        self.assertEqual('Report Card Categories Test 2', categories[0].name)
        self.assertEqual('Report Card Categories Test 1', categories[1].name)
        self.assertEqual('Report Card Categories Test 3', categories[2].name)
    
    def test_evaluations(self):
        card_id = ReportCard.create('Report Card Evaluations Test').id()
        evaluation1 = Evaluation.find_by_id(Evaluation.create('Bob', card_id).id())
        evaluation1 = Evaluation.find_by_id(Evaluation.create('Sue', card_id).id())
        evaluation1 = Evaluation.find_by_id(Evaluation.create('Carly', card_id).id())
        evaluations = ReportCard.find_by_id(card_id).evaluations()
        self.assertEqual(3, len(evaluations))
        self.assertEqual('Bob', evaluations[0].name)
        self.assertEqual('Carly', evaluations[1].name)
        self.assertEqual('Sue', evaluations[2].name)
    
    def test_signatures(self):
        card_id = ReportCard.create('Report Card Signatures Test').id()
        signature1 = Signature.find_by_id(Signature.create('Report Card Signatures Test 1', card_id).id())
        signature1.position = 4
        signature1.put()
        signature2 = Signature.find_by_id(Signature.create('Report Card Signatures Test 2', card_id).id())
        signature2.position = 1
        signature2.put()
        signature3 = Signature.find_by_id(Signature.create('Report Card Signatures Test 3', card_id).id())
        signatures = ReportCard.find_by_id(card_id).signatures()
        self.assertEqual(3, len(signatures))
        self.assertEqual('Report Card Signatures Test 2', signatures[0].name)
        self.assertEqual('Report Card Signatures Test 1', signatures[1].name)
        self.assertEqual('Report Card Signatures Test 3', signatures[2].name)
    
    def test_text_lines(self):
        card_id = ReportCard.create('Report Card Text Lines Test').id()
        text_line1 = TextLine.find_by_id(TextLine.create('Report Card Text Lines Test 1', card_id).id())
        text_line1.position = 4
        text_line1.put()
        text_line2 = TextLine.find_by_id(TextLine.create('Report Card Text Lines Test 2', card_id).id())
        text_line2.position = 1
        text_line2.put()
        text_line3 = TextLine.find_by_id(TextLine.create('Report Card Text Lines Test 3', card_id).id())
        text_lines = ReportCard.find_by_id(card_id).text_lines()
        self.assertEqual(3, len(text_lines))
        self.assertEqual('Report Card Text Lines Test 2', text_lines[0].name)
        self.assertEqual('Report Card Text Lines Test 1', text_lines[1].name)
        self.assertEqual('Report Card Text Lines Test 3', text_lines[2].name)
    
    def test_key_levels(self):
        card_id = ReportCard.create('Report Card Key Levels Test').id()
        key_level1 = EvalKeyLevel.find_by_id(EvalKeyLevel.create('Report Card Key Levels Test 1', 3, card_id).id())
        key_level2 = EvalKeyLevel.find_by_id(EvalKeyLevel.create('Report Card Key Levels Test 2', 1, card_id).id())
        key_level3 = EvalKeyLevel.find_by_id(EvalKeyLevel.create('Report Card Key Levels Test 3', 4, card_id).id())
        key_levels = ReportCard.find_by_id(card_id).key_levels()
        self.assertEqual(3, len(key_levels))
        self.assertEqual('Report Card Key Levels Test 3', key_levels[0].name)
        self.assertEqual('Report Card Key Levels Test 1', key_levels[1].name)
        self.assertEqual('Report Card Key Levels Test 2', key_levels[2].name)