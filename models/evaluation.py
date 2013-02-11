from google.appengine.ext import db
from google.appengine.api import users

from models.base import BaseModel
from models.report_card import ReportCard

MAX_IN_QUERY = 30

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
        items = []
        for category_sublist in [categories[i:i+MAX_IN_QUERY] for i in xrange(0, len(categories), MAX_IN_QUERY)]:
            items.extend(EvalItem.gql("WHERE category IN :1 ORDER BY position ASC", map(lambda i: i.key(), category_sublist)).fetch(100))
        item_data = []
        for item_sublist in [items[i:i+MAX_IN_QUERY] for i in xrange(0, len(items), MAX_IN_QUERY)]:
            item_data.extend(EvalItemData.gql("WHERE eval_item IN :1 AND evaluation = :2", map(lambda i: i.key(), item_sublist), self).fetch(100))
        result = {'items':{}, 'text':{}, 'comments':''}
        for item in items:
            # TODO: base default score on top grade, or allow card owner to set
            result['items'][item.key().id()] = '5'
        for item_datum in item_data:
            result['items'][item_datum.eval_item.key().id()] = item_datum.value
        
        from models.text_line import TextLine
        from models.text_line_data import TextLineData
        lines = self.card.text_lines()
        line_data = []
        for line_sublist in [lines[i:i+MAX_IN_QUERY] for i in xrange(0, len(lines), MAX_IN_QUERY)]:
            line_data.extend(TextLineData.gql("WHERE text_line IN :1 AND evaluation = :2", map(lambda i: i.key(), line_sublist), self).fetch(100))
        for line in lines:
            result['text'][line.key().id()] = ''
        for line_datum in line_data:
            result['text'][line_datum.text_line.key().id()] = line_datum.value
        
        from models.comment_data import CommentData
        comment_data = CommentData.gql("WHERE evaluation = :1", self).fetch(100)
        if len(comment_data) > 0:
            result['comments'] = comment_data[0].value
        return result