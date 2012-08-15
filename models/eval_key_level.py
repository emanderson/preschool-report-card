from google.appengine.ext import db
from google.appengine.api import users

from models.base import BaseModel
from models.report_card import ReportCard

class EvalKeyLevel(BaseModel):
    name = db.StringProperty()
    card = db.ReferenceProperty(ReportCard)
    score = db.IntegerProperty(default=1)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name, score, card_id):
        key_level = EvalKeyLevel(parent=self.report_key())
        key_level.name = name
        key_level.score = score
        card = ReportCard.find_by_id(card_id)
        key_level.card = card
        return key_level.put()