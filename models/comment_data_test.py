import time
from google.appengine.api import users

from test.model_test_case import ModelTestCase
from evaluation import Evaluation
from report_card import ReportCard
from comment_data import CommentData

class CommentDataTest(ModelTestCase):
    def setUp(self):
        super(CommentDataTest, self).setUp()
        self.card_id = ReportCard.create('Comment Data Test Card').id()
        self.evaluation_id = Evaluation.create('Comment Data Test Evaluation', self.card_id).id()

    def test_create_or_update(self):
        first_id = CommentData.create_or_update(self.evaluation_id, 'Comment Data Test Comment').id()
        second_id = CommentData.create_or_update(self.evaluation_id, 'Comment Data Test Comment Updated').id()
        self.assertEqual(first_id, second_id)
        comment_data = CommentData.find_by_id(second_id)
        self.assertEqual('Comment Data Test Comment Updated', comment_data.value)