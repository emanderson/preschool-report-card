from google.appengine.ext import db
from google.appengine.api import users

from models.base import BaseModel

class EvalCategory(BaseModel):
    name = db.StringProperty()
    owner_user_id = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name):
        category = EvalCategory(parent=self.report_key())
        category.name = name
        category.owner_user_id = users.get_current_user().user_id()
        return category.put()
    
    @classmethod
    def list_by_user(self, user=None):
        if not user:
          user = users.get_current_user()
        categories = self.gql("WHERE owner_user_id = :1", user.user_id()).fetch(100)
        return categories
    
    def items(self):
        from models.eval_item import EvalItem
        items = EvalItem.gql("WHERE category = :1", self).fetch(100)
        return items