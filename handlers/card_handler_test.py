import os
import unittest
import webapp2
import webtest
import main
from google.appengine.api import users
from google.appengine.ext import testbed

from card_handler import CardHandler
from models.report_card import ReportCard
from models.app_user import AppUser

class CardHandlerTest(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub()
        
        os.environ['USER_EMAIL'] = 'test@example.com'
        os.environ['USER_ID'] = '123'
    
        self.testapp = webtest.TestApp(main.app)
        
    def tearDown(self):
        self.testbed.deactivate()
    
    def test_main(self):
        response = self.testapp.get('/')
        self.assertEqual(302, response.status_int)
        self.assertRegexpMatches(response.headers['Location'], '/card/list$')
    
    # TODO: second pass of tests with more details
    def test_list(self):
        response = self.testapp.get('/card/list')
        self.assertEqual(200, response.status_int)
    
    def test_add_form(self):
        response = self.testapp.get('/card/add_form')
        self.assertEqual(200, response.status_int)
    
    def test_add(self):
        self.assertEqual(0, len(ReportCard.list_by_user()))
        response = self.testapp.post('/card/add', {'name': 'Add Test Name'})
        self.assertEqual(302, response.status_int)
        self.assertRegexpMatches(response.headers['Location'], '/card/list$')
        cards = ReportCard.list_by_user()
        self.assertEqual(1, len(cards))
        self.assertEqual('Add Test Name', cards[0].name)
    
    def test_edit(self):
        c = ReportCard.create(name='Edit Test Name')
        response = self.testapp.get('/card/%d/edit' % c.id())
        self.assertEqual(200, response.status_int)
    
    def test_preview(self):
        c = ReportCard.create(name='Preview Test Name')
        response = self.testapp.get('/card/%d/preview' % c.id())
        self.assertEqual(200, response.status_int)
    
    def test_add_owner_form(self):
        c = ReportCard.create(name='Add Owner Form Test Name')
        response = self.testapp.get('/card/%d/add_owner_form' % c.id())
        self.assertEqual(200, response.status_int)
    
    def test_add_owner(self):
        u = AppUser.for_user(users.get_current_user())
        u.is_admin = True
        u.put()
    
        c = ReportCard.find_by_id(ReportCard.create(name='Add Owner Test Name').id())
        self.assertEqual(1, len(c.owner_user_id))
        response = self.testapp.post('/card/%d/add_owner' % c.key().id(), {'new_owner_id':'newowner'})
        self.assertEqual(302, response.status_int)
        self.assertRegexpMatches(response.headers['Location'], '/card/list$')
        c = ReportCard.find_by_id(c.key().id())
        self.assertEqual(2, len(c.owner_user_id))
    