import webapp2

from utils.jinja_env import JinjaEnv

class ItemAddFormHandler(webapp2.RequestHandler):
    def get(self, category_id):
        template = JinjaEnv.get().get_template('templates/item_add.html')
        self.response.out.write(template.render({'category_id': category_id}))