import webapp2

from models.report_card import ReportCard
from utils.jinja_env import JinjaEnv

class CardPreviewHandler(webapp2.RequestHandler):
    def get(self, card_id):
        template = JinjaEnv.get().get_template('templates/card_preview.html')
        self.response.out.write(template.render({'card': ReportCard.find_by_id(int(card_id))}))