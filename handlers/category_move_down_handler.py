import webapp2

from models.eval_category import EvalCategory
from models.eval_item import EvalItem
from utils.jinja_env import JinjaEnv

class CategoryMoveDownHandler(webapp2.RequestHandler):
    def post(self, category_id):
        ec = EvalCategory.find_by_id(int(category_id))
        all_categories = ec.card.categories()
        id_list = map(lambda x: x.key().id(), all_categories)
        index = id_list.index(ec.key().id())
        if index < len(all_categories)-1:
            temp = ec.position
            ec.position = all_categories[index+1].position
            all_categories[index+1].position = temp
            ec.save()
            all_categories[index+1].save()
        return webapp2.redirect_to('card-edit', card_id=ec.card.key().id())