import webapp2
from google.appengine.api import users

from models.app_user import AppUser
from models.eval_category import EvalCategory
from utils.jinja_env import JinjaEnv

class FormEditHandler(webapp2.RequestHandler):
    def get(self):
        # TODO: handle this some other way
        AppUser.record_access(users.get_current_user())
        template = JinjaEnv.get().get_template('templates/form_edit_form.html')
        self.response.out.write(template.render({'categories': EvalCategory.list_by_user()}))