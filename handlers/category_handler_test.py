from test.handler_test_case import HandlerTestCase

from category_handler import CategoryHandler
from models.report_card import ReportCard
from models.eval_category import EvalCategory

class CategoryHandlerTest(HandlerTestCase):
    def setUp(self):
        super(CategoryHandlerTest, self).setUp()
        self.card_id = ReportCard.create(name='Category Test Card').id()

    def test_add_form(self):
        response = self.testapp.get('/card/%d/category/add_form' % self.card_id)
        self.assertSuccess(response)
    
    def test_add(self):
        response = self.testapp.get('/card/%d/category/add' % self.card_id, {'name': 'Add Test Name'})
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(1, len(card.categories()))
        self.assertEqual('Add Test Name', card.categories()[0].name)
    
    def test_edit_form(self):
        category_id = EvalCategory.create('Edit Form Test Name', self.card_id).id()
        response = self.testapp.get('/category/%d/edit_form' % category_id)
        self.assertSuccess(response)
    
    def test_edit(self):
        category_id = EvalCategory.create('Edit Test Name', self.card_id).id()
        response = self.testapp.post('/category/%d/edit' % category_id, {'name': 'Edit Test New Name'})
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(1, len(card.categories()))
        self.assertEqual('Edit Test New Name', card.categories()[0].name)
    
    def test_delete_form(self):
        category_id = EvalCategory.create('Delete Form Test Name', self.card_id).id()
        response = self.testapp.get('/category/%d/delete_form' % category_id)
        self.assertSuccess(response)
    
    def test_delete(self):
        category_id = EvalCategory.create('Delete Test Name', self.card_id).id()
        response = self.testapp.post('/category/%d/delete' % category_id)
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(0, len(card.categories()))
    
    def test_move_up(self):
        category1_id = EvalCategory.create('Move Up Test Name 1', self.card_id).id()
        category2_id = EvalCategory.create('Move Up Test Name 2', self.card_id).id()
        response = self.testapp.post('/category/%d/move_up' % category2_id)
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        card = ReportCard.find_by_id(self.card_id)
        categories = card.categories()
        self.assertEqual(2, len(categories))
        self.assertEqual(category2_id, categories[0].key().id())
        self.assertEqual(category1_id, categories[1].key().id())
    
    def test_move_down(self):
        category1_id = EvalCategory.create('Move Up Test Name 1', self.card_id).id()
        category2_id = EvalCategory.create('Move Up Test Name 2', self.card_id).id()
        response = self.testapp.post('/category/%d/move_down' % category1_id)
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        card = ReportCard.find_by_id(self.card_id)
        categories = card.categories()
        self.assertEqual(2, len(categories))
        self.assertEqual(category2_id, categories[0].key().id())
        self.assertEqual(category1_id, categories[1].key().id())
        