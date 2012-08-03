import webapp2

from models.eval_category import EvalCategory
from models.eval_item import EvalItem
from utils.jinja_env import JinjaEnv

class ItemAddHandler(webapp2.RequestHandler):
    def post(self, category_id):
        EvalItem.create(self.request.get('name'), int(category_id))
        return webapp2.redirect_to('card-edit', card_id=EvalCategory.find_by_id(int(category_id)).card.key().id())