import os
import time
import unittest
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import testbed

from app_user import AppUser

class AppUserTest(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub()
        
        os.environ['USER_EMAIL'] = 'test@example.com'
        os.environ['USER_ID'] = '123'
    
    def tearDown(self):
        self.testbed.deactivate()
        
    def test_create(self):
        app_user = AppUser.for_user(users.get_current_user())
        self.assertEqual('test@example.com', app_user.email)
        self.assertEqual('123', app_user.user_id)
    
    def test_for_user(self):
        first_app_user = AppUser.for_user(users.get_current_user())
        first_id = first_app_user.key().id()
        second_app_user = AppUser.for_user(users.get_current_user())
        self.assertEqual(first_id, second_app_user.key().id())
    
    def test_record_access(self):
        app_user = AppUser.for_user(users.get_current_user())
        first_access_date = app_user.first_access
        first_latest_date = app_user.latest_access
        time.sleep(0.1)
        AppUser.record_access(users.get_current_user())
        app_user = AppUser.for_user(users.get_current_user())
        self.assertEqual(first_access_date, app_user.first_access)
        self.assertTrue(app_user.latest_access > first_latest_date)
        