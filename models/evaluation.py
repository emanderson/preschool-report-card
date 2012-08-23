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
        categories = EvalCategory.gql("WHERE card = :1 ORDER BY position ASC", self.card).fetch(100)
        items = EvalItem.gql("WHERE category IN :1 ORDER BY position ASC", map(lambda i: i.key(), categories)).fetch(100)
        item_data = EvalItemData.gql("WHERE eval_item IN :1 AND evaluation = :2", map(lambda i: i.key(), items), self).fetch(100)
        result = {'items':{}}
        for item in items:
            result['items'][item.key().id()] = ''
        for item_datum in item_data:
            result['items'][item_datum.eval_item.key().id()] = item_datum.value
        return result