from test.handler_test_case import HandlerTestCase

from signature_handler import SignatureHandler
from models.report_card import ReportCard
from models.signature import Signature

class SignatureHandlerTest(HandlerTestCase):
    def setUp(self):
        super(SignatureHandlerTest, self).setUp()
        self.card_id = ReportCard.create(name='Signature Test Card').id()

    def test_add_form(self):
        response = self.testapp.get('/card/%d/signature/add_form' % self.card_id)
        self.assertSuccess(response)
    
    def test_add(self):
        response = self.testapp.get('/card/%d/signature/add' % self.card_id, {'name': 'Add Test Name'})
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(1, len(card.signatures()))
        self.assertEqual('Add Test Name', card.signatures()[0].name)
    
    def test_edit_form(self):
        signature_id = Signature.create('Edit Form Test Name', self.card_id).id()
        response = self.testapp.get('/signature/%d/edit_form' % signature_id)
        self.assertSuccess(response)
    
    def test_edit(self):
        signature_id = Signature.create('Edit Test Name', self.card_id).id()
        response = self.testapp.post('/signature/%d/edit' % signature_id, {'name': 'Edit Test New Name'})
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(1, len(card.signatures()))
        self.assertEqual('Edit Test New Name', card.signatures()[0].name)
    
    def test_delete_form(self):
        signature_id = Signature.create('Delete Form Test Name', self.card_id).id()
        response = self.testapp.get('/signature/%d/delete_form' % signature_id)
        self.assertSuccess(response)
    
    def test_delete(self):
        signature_id = Signature.create('Delete Test Name', self.card_id).id()
        response = self.testapp.post('/signature/%d/delete' % signature_id)
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        self.assertEqual(0, len(card.signatures()))
    
    def test_move_up(self):
        signature1_id = Signature.create('Move Up Test Name 1', self.card_id).id()
        signature2_id = Signature.create('Move Up Test Name 2', self.card_id).id()
        self.assertRaises(Exception, self.testapp.post, '/signature/%d/move_up' % signature1_id)
        response = self.testapp.post('/signature/%d/move_up' % signature2_id)
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        signatures = card.signatures()
        self.assertEqual(2, len(signatures))
        self.assertEqual(signature2_id, signatures[0].key().id())
        self.assertEqual(signature1_id, signatures[1].key().id())
    
    def test_move_down(self):
        signature1_id = Signature.create('Move Up Test Name 1', self.card_id).id()
        signature2_id = Signature.create('Move Up Test Name 2', self.card_id).id()
        self.assertRaises(Exception, self.testapp.post, '/signature/%d/move_down' % signature2_id)
        response = self.testapp.post('/signature/%d/move_down' % signature1_id)
        self.assertSuccess(response)
        card = ReportCard.find_by_id(self.card_id)
        signatures = card.signatures()
        self.assertEqual(2, len(signatures))
        self.assertEqual(signature2_id, signatures[0].key().id())
        self.assertEqual(signature1_id, signatures[1].key().id())
        