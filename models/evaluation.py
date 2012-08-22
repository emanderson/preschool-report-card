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