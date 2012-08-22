import webapp2
from google.appengine.api import users

from models.app_user import AppUser
from models.report_card import ReportCard
from utils.jinja_env import JinjaEnv

class EvalHandler(webapp2.RequestHandler):
    def list(self, card_id):
        # TODO: handle this some other way
        AppUser.record_access(users.get_current_user())
        current_user = AppUser.for_user(users.get_current_user())
        template = JinjaEnv.get().get_template('templates/eval_list.html')
        self.response.out.write(template.render({'card': ReportCard.find_by_id(int(card_id)), 'current_user': current_user}))