import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from signature import Signature
from report_card import ReportCard

class SignatureTest(ModelTestCase):
    def setUp(self):
        super(SignatureTest, self).setUp()
        self.card_id = ReportCard.create('Signature Test Card').id()
    
    def test_create(self):
        signature_id = Signature.create('Signature Test', self.card_id).id()
        signature = Signature.find_by_id(signature_id)
        self.assertEqual('Signature Test', signature.name)
        self.assertEqual(self.card_id, signature.card.key().id())