from google.appengine.ext import db

from models.base import BaseModel
from models.evaluation import Evaluation

class CommentData(BaseModel):
    evaluation = db.ReferenceProperty(Evaluation)
    value = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create_or_update(self, evaluation_id, value):
        evaluation = Evaluation.find_by_id(evaluation_id)
        
        data = CommentData.gql('WHERE evaluation = :1', evaluation).fetch(1)
        if len(data) == 0:
            data = CommentData(parent=self.report_key())
            data.evaluation = evaluation
        else:
            data = data[0]
        
        data.value = value
        return data.put()
            