from google.appengine.ext import db
from google.appengine.api import users

from models.base import BaseModel
from models.report_card import ReportCard

class Evaluation(BaseModel):
    name = db.StringProperty()
    card = db.ReferenceProperty(ReportCard)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name, card_id):
        eval = Evaluation(parent=self.report_key())
        eval.name = name
        card = ReportCard.find_by_id(card_id)
        eval.card = card
        return eval.put()
    
    def all_data(self):
        from models.eval_category import EvalCategory
        from models.eval_item import EvalItem
        from models.eval_item_data import EvalItemData
        categories = self.card.categories()
        items = EvalItem.gql("WHERE category IN :1 ORDER BY position ASC", map(lambda i: i.key(), categories)).fetch(100)
        item_data = EvalItemData.gql("WHERE eval_item IN :1 AND evaluation = :2", map(lambda i: i.key(), items), self).fetch(100)
        result = {'items':{}, 'text':{}, 'comments':''}
        for item in items:
            result['items'][item.key().id()] = ''
        for item_datum in item_data:
            result['items'][item_datum.eval_item.key().id()] = item_datum.value
        
        from models.text_line import TextLine
        from models.text_line_data import TextLineData
        lines = self.card.text_lines()
        line_data = TextLineData.gql("WHERE text_line IN :1 AND evaluation = :2", map(lambda i: i.key(), lines), self).fetch(100)
        for line in lines:
            result['text'][line.key().id()] = ''
        for line_datum in line_data:
            result['text'][line_datum.text_line.key().id()] = line_datum.value
        
        from models.comment_data import CommentData
        comment_data = CommentData.gql("WHERE evaluation = :1", self).fetch(100)
        if len(comment_data) > 0:
            result['comments'] = comment_data[0].value
        return result