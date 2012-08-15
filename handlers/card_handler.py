import webapp2
from google.appengine.api import users

from models.app_user import AppUser
from models.report_card import ReportCard
from utils.jinja_env import JinjaEnv

class CardHandler(webapp2.RequestHandler):
    def list(self):
        # TODO: handle this some other way
        AppUser.record_access(users.get_current_user())
        template = JinjaEnv.get().get_template('templates/card_list.html')
        self.response.out.write(template.render({'cards': ReportCard.list_by_user()}))

    def add_form(self):
        template = JinjaEnv.get().get_template('templates/card_add.html')
        self.response.out.write(template.render({}))
        
    def add(self):
        ReportCard.create(self.request.get('name'))
        return webapp2.redirect_to('card-list')

    def edit(self, card_id):
        # TODO: handle this some other way
        AppUser.record_access(users.get_current_user())
        template = JinjaEnv.get().get_template('templates/card_edit_form.html')
        self.response.out.write(template.render({'card': ReportCard.find_by_id(int(card_id))}))

    def preview(self, card_id):
        template = JinjaEnv.get().get_template('templates/card_preview.html')
        self.response.out.write(template.render({'card': ReportCard.find_by_id(int(card_id))}))