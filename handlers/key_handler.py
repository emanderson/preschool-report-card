import webapp2

from utils.jinja_env import JinjaEnv
from models.eval_key_level import EvalKeyLevel
from models.report_card import ReportCard

class KeyHandler(webapp2.RequestHandler):
    def add_form(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/key_level/add_form.html')
            self.response.out.write(template.render({'card_id': card_id}))
    
    def add(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            key_level_id = EvalKeyLevel.create(self.request.get('name'), int(self.request.get('score')), int(card_id)).id()
            key_level = EvalKeyLevel.find_by_id(key_level_id)
            template = JinjaEnv.get().get_template('templates/key_level/edit_row.html')
            self.response.out.write(template.render({'key_level': key_level}))
    
    def edit_form(self, key_level_id):
        key_level = EvalKeyLevel.find_by_id(int(key_level_id))
        card = key_level.card
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/key_level/edit_form.html')
            self.response.out.write(template.render({'key_level_id': key_level_id, 'key_level': key_level}))
        
    def edit(self, key_level_id):
        key_level = EvalKeyLevel.find_by_id(int(key_level_id))
        card = key_level.card
        if card.is_authorized():
            key_level.name = self.request.get('name')
            key_level.score = int(self.request.get('score'))
            key_level.save()
            template = JinjaEnv.get().get_template('templates/key_level/edit_row.html')
            self.response.out.write(template.render({'key_level': key_level}))
    
    def delete_form(self, key_level_id):
        key_level = EvalKeyLevel.find_by_id(int(key_level_id))
        card = key_level.card
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/key_level/delete_form.html')
            self.response.out.write(template.render({'key_level_id': key_level_id, 'key_level': key_level}))
        
    def delete(self, key_level_id):
        key_level = EvalKeyLevel.find_by_id(int(key_level_id))
        card = key_level.card
        if card.is_authorized():
            card_id = key_level.card.key().id()
            key_level.delete()