import webapp2

from models.eval_category import EvalCategory
from utils.jinja_env import JinjaEnv

class CategoryAddHandler(webapp2.RequestHandler):
    def post(self):
        EvalCategory.create(self.request.get('name'))
        return webapp2.redirect_to('form-edit')