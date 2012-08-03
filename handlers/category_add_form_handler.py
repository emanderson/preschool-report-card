import webapp2

from utils.jinja_env import JinjaEnv

class CategoryAddFormHandler(webapp2.RequestHandler):
    def get(self, card_id):
        template = JinjaEnv.get().get_template('templates/category_add.html')
        self.response.out.write(template.render({'card_id': card_id}))