from google.appengine.ext import db

from models.base import BaseModel
from models.eval_item import EvalItem
from models.evaluation import Evaluation

class EvalItemData(BaseModel):
    eval_item = db.ReferenceProperty(EvalItem)
    evaluation = db.ReferenceProperty(Evaluation)
    value = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create_or_update(self, eval_item_id, evaluation_id, value):
        item = EvalItem.find_by_id(eval_item_id)
        evaluation = Evaluation.find_by_id(evaluation_id)
        
        data = EvalItemData.gql('WHERE eval_item = :1 AND evaluation = :2', item, evaluation).fetch(1)
        if len(data) == 0:
            data = EvalItemData(parent=self.report_key())
            data.eval_item = item
            data.evaluation = evaluation
        else:
            data = data[0]
        
        data.value = value
        return data.put()
            