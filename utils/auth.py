from google.appengine.api import users

class Auth(object):
    @classmethod
    def logout_url(self):
        return users.create_logout_url("/form/edit")