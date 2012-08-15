import webapp2

from models.eval_category import EvalCategory
from models.eval_item import EvalItem
from utils.jinja_env import JinjaEnv

class ItemDeleteHandler(webapp2.RequestHandler):
    def post(self, item_id):
        ei = EvalItem.find_by_id(int(item_id))
        card_id = ei.category.card.key().id()
        ei.delete()
        return webapp2.redirect_to('card-edit', card_id=card_id)