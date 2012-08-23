import webtest
import main

from models.app_user import AppUser
from base_test_case import BaseTestCase

class HandlerTestCase(BaseTestCase):
    def setUp(self):
        super(HandlerTestCase, self).setUp()
        self.testapp = webtest.TestApp(main.app)
    
    def assertSuccess(self, response):
        self.assertEqual(200, response.status_int)
    
    def assertRedirect(self, pattern, response):
        self.assertEqual(302, response.status_int)
        self.assertRegexpMatches(response.headers['Location'], pattern)
    