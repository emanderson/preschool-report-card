from google.appengine.ext import db

from models.base import BaseModel

class AppUser(BaseModel):
    email = db.StringProperty()
    user_id = db.StringProperty()
    is_admin = db.BooleanProperty(default=False)
    first_access = db.DateTimeProperty(auto_now_add=True)
    latest_access = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, user):
        app_user = AppUser(parent=self.report_key())
        app_user.email = user.email()
        app_user.user_id = user.user_id()
        return app_user.put()
    
    @classmethod
    def record_access(self, user):
        app_user = self.gql("WHERE user_id = :1", user.user_id()).fetch(1)
        if app_user:
            app_user[0].put()
        else:
            self.create(user)