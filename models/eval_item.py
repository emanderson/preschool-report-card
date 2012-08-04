from google.appengine.ext import db

from models.base import BaseModel
from models.eval_category import EvalCategory

class EvalItem(BaseModel):
    name = db.StringProperty()
    category = db.ReferenceProperty(EvalCategory)
    position = db.IntegerProperty(default=1)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name, category_id):
        item = EvalItem(parent=self.report_key())
        item.name = name
        category = EvalCategory.find_by_id(category_id)
        item.category = category
        if len(category.items()) > 0:
            item.position = category.items()[-1].position+1
        return item.put()