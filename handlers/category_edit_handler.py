import webapp2

from models.eval_category import EvalCategory
from models.eval_item import EvalItem
from utils.jinja_env import JinjaEnv

class CategoryEditHandler(webapp2.RequestHandler):
    def post(self, category_id):
        ec = EvalCategory.find_by_id(int(category_id))
        ec.name = self.request.get('name')
        ec.save()
        return webapp2.redirect_to('card-edit', card_id=ec.card.key().id())