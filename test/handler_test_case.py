import os
import unittest
import webapp2
import webtest
import main
from google.appengine.api import users
from google.appengine.ext import testbed

from models.app_user import AppUser

class HandlerTestCase(unittest.TestCase):
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
    
    def assertSuccess(self, response):
        self.assertEqual(200, response.status_int)
    
    def assertRedirect(self, pattern, response):
        self.assertEqual(302, response.status_int)
        self.assertRegexpMatches(response.headers['Location'], pattern)
    
    def makeAdmin(self, user=None):
        if not user:
            user = users.get_current_user()
        u = AppUser.for_user(user)
        u.is_admin = True
        u.put()
    