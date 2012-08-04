from google.appengine.ext import db
from google.appengine.api import users

from models.base import BaseModel
from models.report_card import ReportCard

class EvalCategory(BaseModel):
    name = db.StringProperty()
    card = db.ReferenceProperty(ReportCard)
    position = db.IntegerProperty(default=1)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name, card_id):
        category = EvalCategory(parent=self.report_key())
        category.name = name
        card = ReportCard.find_by_id(card_id)
        category.card = card
        if len(card.categories()) > 0:
            category.position = card.categories()[-1].position+1
        return category.put()
    
    def items(self):
        from models.eval_item import EvalItem
        items = EvalItem.gql("WHERE category = :1 ORDER BY position ASC", self).fetch(100)
        return items