from google.appengine.ext import db

from models.base import BaseModel

class EvalCategory(BaseModel):
    name = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name):
        category = EvalCategory(parent=self.report_key())
        category.name = name
        return category.put()
    
    def items(self):
        from models.eval_item import EvalItem
        items = EvalItem.gql("WHERE category = :1", self).fetch(100)
        return items