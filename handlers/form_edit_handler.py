import webapp2

from models.eval_category import EvalCategory
from utils.jinja_env import JinjaEnv

class FormEditHandler(webapp2.RequestHandler):
    def get(self):
        template = JinjaEnv.get().get_template('templates/form_edit_form.html')
        self.response.out.write(template.render({'categories': EvalCategory.list_by_user()}))