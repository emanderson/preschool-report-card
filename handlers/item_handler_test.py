from test.handler_test_case import HandlerTestCase

from item_handler import ItemHandler
from models.report_card import ReportCard
from models.eval_category import EvalCategory
from models.eval_item import EvalItem

class ItemHandlerTest(HandlerTestCase):
    def setUp(self):
        super(ItemHandlerTest, self).setUp()
        self.card_id = ReportCard.create(name='Item Test Card').id()
        self.category_id = EvalCategory.create('Item Test Category', self.card_id).id()

    def test_add_form(self):
        response = self.testapp.get('/category/%d/item/add_form' % self.category_id)
        self.assertSuccess(response)
    
    def test_add(self):
        response = self.testapp.get('/category/%d/item/add' % self.category_id, {'name': 'Add Test Name'})
        self.assertSuccess(response)
        category = ReportCard.find_by_id(self.card_id).categories()[0]
        self.assertEqual(1, len(category.items()))
        self.assertEqual('Add Test Name', category.items()[0].name)
    
    def test_edit_form(self):
        item_id = EvalItem.create('Edit Form Test Name', self.category_id).id()
        response = self.testapp.get('/item/%d/edit_form' % item_id)
        self.assertSuccess(response)
    
    def test_edit(self):
        item_id = EvalItem.create('Edit Test Name', self.category_id).id()
        response = self.testapp.post('/item/%d/edit' % item_id, {'name': 'Edit Test New Name'})
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        category = ReportCard.find_by_id(self.card_id).categories()[0]
        self.assertEqual(1, len(category.items()))
        self.assertEqual('Edit Test New Name', category.items()[0].name)
    
    def test_delete_form(self):
        item_id = EvalItem.create('Delete Form Test Name', self.category_id).id()
        response = self.testapp.get('/item/%d/delete_form' % item_id)
        self.assertSuccess(response)
    
    def test_delete(self):
        item_id = EvalItem.create('Delete Test Name', self.category_id).id()
        response = self.testapp.post('/item/%d/delete' % item_id)
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        category = ReportCard.find_by_id(self.card_id).categories()[0]
        self.assertEqual(0, len(category.items()))
    
    def test_move_up(self):
        item1_id = EvalItem.create('Move Up Test Name 1', self.category_id).id()
        item2_id = EvalItem.create('Move Up Test Name 2', self.category_id).id()
        response = self.testapp.post('/item/%d/move_up' % item2_id)
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        category = ReportCard.find_by_id(self.card_id).categories()[0]
        items = category.items()
        self.assertEqual(2, len(items))
        self.assertEqual(item2_id, items[0].key().id())
        self.assertEqual(item1_id, items[1].key().id())
    
    def test_move_down(self):
        item1_id = EvalItem.create('Move Up Test Name 1', self.category_id).id()
        item2_id = EvalItem.create('Move Up Test Name 2', self.category_id).id()
        response = self.testapp.post('/item/%d/move_down' % item1_id)
        self.assertRedirect('/card/%d/edit' % self.card_id, response)
        category = ReportCard.find_by_id(self.card_id).categories()[0]
        items = category.items()
        self.assertEqual(2, len(items))
        self.assertEqual(item2_id, items[0].key().id())
        self.assertEqual(item1_id, items[1].key().id())
        