from google.appengine.ext import db
from google.appengine.api import users

from models.base import BaseModel
from models.app_user import AppUser

class ReportCard(BaseModel):
    name = db.StringProperty()
    owner_user_id = db.ListProperty(str)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name):
        card = ReportCard(parent=self.report_key())
        card.name = name
        card.owner_user_id = [users.get_current_user().user_id()]
        return card.put()
    
    @classmethod
    def list_by_user(self, user=None):
        if not user:
          user = users.get_current_user()
        app_user = AppUser.for_user(user)
        if app_user.is_admin:
            cards = self.list()
        else:
            cards = self.gql("WHERE owner_user_id = :1", user.user_id()).fetch(100)
        return cards
    
    def categories(self):
        from models.eval_category import EvalCategory
        items = EvalCategory.gql("WHERE card = :1 ORDER BY position ASC", self).fetch(100)
        return items
    
    def key_levels(self):
        from models.eval_key_level import EvalKeyLevel
        levels = EvalKeyLevel.gql("WHERE card = :1 ORDER BY score DESC", self).fetch(100)
        return levels