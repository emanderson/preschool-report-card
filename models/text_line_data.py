from google.appengine.ext import db

from models.base import BaseModel
from models.text_line import TextLine
from models.evaluation import Evaluation

class TextLineData(BaseModel):
    text_line = db.ReferenceProperty(TextLine)
    evaluation = db.ReferenceProperty(Evaluation)
    value = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create_or_update(self, text_line_id, evaluation_id, value):
        line = TextLine.find_by_id(text_line_id)
        evaluation = Evaluation.find_by_id(evaluation_id)
        
        data = TextLineData.gql('WHERE text_line = :1 AND evaluation = :2', line, evaluation).fetch(1)
        if len(data) == 0:
            data = TextLineData(parent=self.report_key())
            data.text_line = line
            data.evaluation = evaluation
        else:
            data = data[0]
        
        data.value = value
        return data.put()
            