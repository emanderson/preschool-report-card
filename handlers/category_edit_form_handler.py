import webapp2

from models.eval_category import EvalCategory
from utils.jinja_env import JinjaEnv

class CategoryEditFormHandler(webapp2.RequestHandler):
    def get(self, category_id):
        template = JinjaEnv.get().get_template('templates/category_edit_form.html')
        self.response.out.write(template.render({'category_id': category_id, 'category': EvalCategory.find_by_id(int(category_id))}))