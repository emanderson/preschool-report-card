import webapp2
from google.appengine.api import users

from models.app_user import AppUser
from models.report_card import ReportCard
from models.evaluation import Evaluation
from models.eval_item_data import EvalItemData
from models.text_line_data import TextLineData
from models.comment_data import CommentData
from utils.jinja_env import JinjaEnv

class EvalHandler(webapp2.RequestHandler):
    def list(self, card_id):
        # TODO: handle this some other way
        AppUser.record_access(users.get_current_user())
        current_user = AppUser.for_user(users.get_current_user())
        template = JinjaEnv.get().get_template('templates/eval/list.html')
        self.response.out.write(template.render({'card': ReportCard.find_by_id(int(card_id)), 'current_user': current_user}))
        
    def add_form(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/eval/add_form.html')
            self.response.out.write(template.render({'card': card}))
        
    def add(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            Evaluation.create(self.request.get('name'), int(card_id))
            return webapp2.redirect_to('eval-list', card_id=int(card_id))

    def fill(self, eval_id):
        eval = Evaluation.find_by_id(int(eval_id))
        if eval.card.is_authorized():
            template = JinjaEnv.get().get_template('templates/eval/fill.html')
            self.response.out.write(template.render({'eval': eval, 'data': eval.all_data()}))

    def preview(self, eval_id):
        eval = Evaluation.find_by_id(int(eval_id))
        if eval.card.is_authorized():
            template = JinjaEnv.get().get_template('templates/eval/preview.html')
            self.response.out.write(template.render({'eval': eval, 'data': eval.all_data()}))
    
    def save(self, eval_id):
        eval = Evaluation.find_by_id(int(eval_id))
        if eval.card.is_authorized():
            for cat in eval.card.categories():
                for item in cat.items():
                    val = self.request.get('item_%s_score' % item.key().id())
                    if val is not None:
                        EvalItemData.create_or_update(item.key().id(), int(eval_id), val)
            for line in eval.card.text_lines():
                val = self.request.get('text_%s_value' % line.key().id())
                if val is not None:
                    TextLineData.create_or_update(line.key().id(), int(eval_id), val)
            val = self.request.get('comments')
            if val is not None:
                CommentData.create_or_update(int(eval_id), val)
            return webapp2.redirect_to('eval-fill', eval_id=int(eval_id))