import webapp2

from utils.jinja_env import JinjaEnv

class CardAddFormHandler(webapp2.RequestHandler):
    def get(self):
        template = JinjaEnv.get().get_template('templates/card_add.html')
        self.response.out.write(template.render({}))