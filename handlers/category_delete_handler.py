import webapp2

from models.eval_category import EvalCategory
from models.eval_item import EvalItem
from utils.jinja_env import JinjaEnv

class CategoryDeleteHandler(webapp2.RequestHandler):
    def post(self, category_id):
        ec = EvalCategory.find_by_id(int(category_id))
        card_id = ec.card.key().id()
        ec.delete()
        return webapp2.redirect_to('card-edit', card_id=card_id)