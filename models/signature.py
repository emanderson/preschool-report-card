from google.appengine.ext import db
from google.appengine.api import users

from models.base import BaseModel
from models.report_card import ReportCard

class Signature(BaseModel):
    name = db.StringProperty()
    card = db.ReferenceProperty(ReportCard)
    position = db.IntegerProperty(default=1)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name, card_id):
        signature = Signature(parent=self.report_key())
        signature.name = name
        card = ReportCard.find_by_id(card_id)
        signature.card = card
        if len(card.signatures()) > 0:
            signature.position = card.signatures()[-1].position+1
        return signature.put()