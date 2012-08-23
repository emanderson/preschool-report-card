from test.handler_test_case import HandlerTestCase

from card_handler import CardHandler
from models.report_card import ReportCard

class CardHandlerTest(HandlerTestCase):
    def test_main(self):
        response = self.testapp.get('/')
        self.assertRedirect('/card/list$', response)
    
    # TODO: second pass of tests with more details
    def test_list(self):
        response = self.testapp.get('/card/list')
        self.assertSuccess(response)
    
    def test_add_form(self):
        response = self.testapp.get('/card/add_form')
        self.assertEqual(200, response.status_int)
    
    def test_add(self):
        self.assertEqual(0, len(ReportCard.list_by_user()))
        response = self.testapp.post('/card/add', {'name': 'Add Test Name'})
        self.assertRedirect('/card/list$', response)
        cards = ReportCard.list_by_user()
        self.assertEqual(1, len(cards))
        self.assertEqual('Add Test Name', cards[0].name)
    
    def test_edit(self):
        c = ReportCard.create(name='Edit Test Name')
        response = self.testapp.get('/card/%d/edit' % c.id())
        self.assertSuccess(response)
    
    def test_preview(self):
        c = ReportCard.create(name='Preview Test Name')
        response = self.testapp.get('/card/%d/preview' % c.id())
        self.assertSuccess(response)
    
    def test_add_owner_form(self):
        self.makeAdmin()
        c = ReportCard.create(name='Add Owner Form Test Name')
        response = self.testapp.get('/card/%d/add_owner_form' % c.id())
        self.assertSuccess(response)
    
    def test_add_owner(self):
        self.makeAdmin()
        c = ReportCard.find_by_id(ReportCard.create(name='Add Owner Test Name').id())
        self.assertEqual(1, len(c.owner_user_id))
        response = self.testapp.post('/card/%d/add_owner' % c.key().id(), {'new_owner_id':'newowner'})
        self.assertRedirect('/card/list$', response)
        c = ReportCard.find_by_id(c.key().id())
        self.assertEqual(2, len(c.owner_user_id))
    