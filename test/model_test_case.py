import os
import time
import unittest
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import testbed

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub()
        
        os.environ['USER_EMAIL'] = 'test@example.com'
        os.environ['USER_ID'] = '123'
    
    def tearDown(self):
        self.testbed.deactivate()