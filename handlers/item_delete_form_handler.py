import webapp2

from models.eval_item import EvalItem
from utils.jinja_env import JinjaEnv

class ItemDeleteFormHandler(webapp2.RequestHandler):
    def get(self, item_id):
        template = JinjaEnv.get().get_template('templates/item_delete.html')
        self.response.out.write(template.render({'item_id': item_id, 'item': EvalItem.find_by_id(int(item_id))}))