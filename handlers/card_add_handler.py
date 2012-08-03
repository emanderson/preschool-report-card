import webapp2

from models.report_card import ReportCard
from utils.jinja_env import JinjaEnv

class CardAddHandler(webapp2.RequestHandler):
    def post(self):
        ReportCard.create(self.request.get('name'))
        return webapp2.redirect_to('card-list')