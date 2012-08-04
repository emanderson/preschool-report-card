import webapp2

from models.eval_category import EvalCategory
from models.eval_item import EvalItem
from utils.jinja_env import JinjaEnv

class ItemMoveUpHandler(webapp2.RequestHandler):
    def post(self, item_id):
        ei = EvalItem.find_by_id(int(item_id))
        all_items = ei.category.items()
        id_list = map(lambda x: x.key().id(), all_items)
        index = id_list.index(ei.key().id())
        if index >= 1:
            temp = ei.position
            ei.position = all_items[index-1].position
            all_items[index-1].position = temp
            ei.save()
            all_items[index-1].save()
        return webapp2.redirect_to('card-edit', card_id=ei.category.card.key().id())