from google.appengine.ext import db
from google.appengine.api import users

from models.base import BaseModel
from models.report_card import ReportCard

class TextLine(BaseModel):
    name = db.StringProperty()
    card = db.ReferenceProperty(ReportCard)
    position = db.IntegerProperty(default=1)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name, card_id):
        text_line = TextLine(parent=self.report_key())
        text_line.name = name
        card = ReportCard.find_by_id(card_id)
        text_line.card = card
        if len(card.text_lines()) > 0:
            text_line.position = card.text_lines()[-1].position+1
        return text_line.put()