from test.handler_test_case import HandlerTestCase

from models.report_card import ReportCard
from models.evaluation import Evaluation
from models.eval_category import EvalCategory
from models.eval_item import EvalItem
from models.text_line import TextLine

class EvalHandlerTest(HandlerTestCase):
    def setUp(self):
        super(EvalHandlerTest, self).setUp()
        self.card_id = ReportCard.create(name='Eval Test Card').id()

    # TODO: second pass of tests with more details
    def test_list(self):
        response = self.testapp.get('/card/%d/eval/list' % self.card_id)
        self.assertSuccess(response)
    
    def test_add_form(self):
        response = self.testapp.get('/card/%d/eval/add_form' % self.card_id)
        self.assertEqual(200, response.status_int)
    
    def test_add(self):
        response = self.testapp.post('/card/%d/eval/add' % self.card_id, {'name': 'Add Test Name'})
        self.assertRedirect('/card/\d*/eval/list$', response)
        evals = ReportCard.find_by_id(self.card_id).evaluations()
        self.assertEqual(1, len(evals))
        self.assertEqual('Add Test Name', evals[0].name)
    
    def test_fill(self):
        e = Evaluation.create('Edit Test Name', self.card_id)
        response = self.testapp.get('/eval/%d/fill' % e.id())
        self.assertSuccess(response)
    
    def test_preview(self):
        e = Evaluation.create('Preview Test Name', self.card_id)
        category1_id = EvalCategory.create('Eval Preview Test Cat 1', self.card_id).id()
        category2_id = EvalCategory.create('Eval Preview Test Cat 2', self.card_id).id()
        item1_id = EvalItem.create('Eval Preview Test Item 1', category1_id).id()
        item2_id = EvalItem.create('Eval Preview Test Item 2', category1_id).id()
        item3_id = EvalItem.create('Eval Preview Test Item 3', category2_id).id()
        text_line1_id = TextLine.create('Eval Preview Test Text Line 1', self.card_id).id()
        text_line2_id = TextLine.create('Eval Preview Test Text Line 2', self.card_id).id()
        response = self.testapp.get('/eval/%d/preview' % e.id())
        self.assertSuccess(response)
    
    def test_save(self):
        eval_id = Evaluation.create('Edit Test Name', self.card_id).id()
        category1_id = EvalCategory.create('Eval Save Test Cat 1', self.card_id).id()
        category2_id = EvalCategory.create('Eval Save Test Cat 2', self.card_id).id()
        item1_id = EvalItem.create('Eval Save Test Item 1', category1_id).id()
        item2_id = EvalItem.create('Eval Save Test Item 2', category1_id).id()
        item3_id = EvalItem.create('Eval Save Test Item 3', category2_id).id()
        text_line1_id = TextLine.create('Eval Save Test Text Line 1', self.card_id).id()
        text_line2_id = TextLine.create('Eval Save Test Text Line 2', self.card_id).id()
        
        response = self.testapp.post('/eval/%d/save' % eval_id, 
            {'comments': 'Comments', 
             'item_%d_score' % item1_id: '1', 
             'item_%d_score' % item2_id: '2', 
             'item_%d_score' % item3_id: '3',
             'text_%d_value' % text_line1_id: 'Text 1',
             'text_%d_value' % text_line2_id: 'Text 2',
            }
        )
        self.assertRedirect('/eval/\d*/fill$', response)
        eval = Evaluation.find_by_id(eval_id)
        data = eval.all_data()
        self.assertEqual('Comments', data['comments'])
        self.assertEqual('1', data['items'][item1_id])
        self.assertEqual('2', data['items'][item2_id])
        self.assertEqual('3', data['items'][item3_id])
        self.assertEqual('Text 1', data['text'][text_line1_id])
        self.assertEqual('Text 2', data['text'][text_line2_id])
        
    