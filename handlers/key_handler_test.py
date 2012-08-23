from test.handler_test_case import HandlerTestCase

from models.report_card import ReportCard
from models.eval_key_level import EvalKeyLevel

class KeyLevelHandlerTest(HandlerTestCase):
    def setUp(self):
        super(KeyLevelHandlerTest, self).setUp()
        self.card_id = ReportCard.create(name='Key Level Test Card').id()

    def test_add_form(self):
        response = self.testapp.get('/card/%d/key_level/add_form' % self.card_id)
        self.assertSuccess(response)
    
    def test_add(self):
        response = self.testapp.get('/card/%d/key_level/add' % self.card_id, {'name': 'Add Test Name', 'score': 1})
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(1, len(card.key_levels()))
        self.assertEqual('Add Test Name', card.key_levels()[0].name)
        self.assertEqual(1, card.key_levels()[0].score)
    
    def test_edit_form(self):
        key_level_id = EvalKeyLevel.create('Edit Form Test Name', 1, self.card_id).id()
        response = self.testapp.get('/key_level/%d/edit_form' % key_level_id)
        self.assertSuccess(response)
    
    def test_edit(self):
        key_level_id = EvalKeyLevel.create('Edit Test Name', 1, self.card_id).id()
        response = self.testapp.post('/key_level/%d/edit' % key_level_id, {'name': 'Edit Test New Name', 'score': 2})
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(1, len(card.key_levels()))
        self.assertEqual('Edit Test New Name', card.key_levels()[0].name)
        self.assertEqual(2, card.key_levels()[0].score)
    
    def test_delete_form(self):
        key_level_id = EvalKeyLevel.create('Delete Form Test Name', 1, self.card_id).id()
        response = self.testapp.get('/key_level/%d/delete_form' % key_level_id)
        self.assertSuccess(response)
    
    def test_delete(self):
        key_level_id = EvalKeyLevel.create('Delete Test Name', 1, self.card_id).id()
        response = self.testapp.post('/key_level/%d/delete' % key_level_id)
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(0, len(card.key_levels()))