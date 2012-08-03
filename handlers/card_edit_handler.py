import webapp2
from google.appengine.api import users

from models.app_user import AppUser
from models.report_card import ReportCard
from utils.jinja_env import JinjaEnv

class CardEditHandler(webapp2.RequestHandler):
    def get(self, card_id):
        # TODO: handle this some other way
        AppUser.record_access(users.get_current_user())
        template = JinjaEnv.get().get_template('templates/card_edit_form.html')
        self.response.out.write(template.render({'card': ReportCard.find_by_id(int(card_id))}))