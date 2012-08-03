import webapp2

from models.eval_category import EvalCategory
from utils.jinja_env import JinjaEnv

class CategoryAddHandler(webapp2.RequestHandler):
    def post(self, card_id):
        EvalCategory.create(self.request.get('name'), int(card_id))
        return webapp2.redirect_to('card-edit', card_id=card_id)