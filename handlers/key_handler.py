import webapp2

from utils.jinja_env import JinjaEnv
from models.eval_key_level import EvalKeyLevel

class KeyHandler(webapp2.RequestHandler):
    def add_form(self, card_id):
        template = JinjaEnv.get().get_template('templates/key_level_add_form.html')
        self.response.out.write(template.render({'card_id': card_id}))
    
    def add(self, card_id):
        EvalKeyLevel.create(self.request.get('name'), int(self.request.get('score')), int(card_id))
        return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def edit_form(self, key_level_id):
        template = JinjaEnv.get().get_template('templates/key_level_edit_form.html')
        self.response.out.write(template.render({'key_level_id': key_level_id, 'key_level': EvalKeyLevel.find_by_id(int(key_level_id))}))
        
    def edit(self, key_level_id):
        ekl = EvalKeyLevel.find_by_id(int(key_level_id))
        ekl.name = self.request.get('name')
        ekl.score = int(self.request.get('score'))
        ekl.save()
        return webapp2.redirect_to('card-edit', card_id=ekl.card.key().id())
    
    def delete_form(self, key_level_id):
        template = JinjaEnv.get().get_template('templates/key_level_delete_form.html')
        self.response.out.write(template.render({'key_level_id': key_level_id, 'key_level': EvalKeyLevel.find_by_id(int(key_level_id))}))
        
    def delete(self, key_level_id):
        ekl = EvalKeyLevel.find_by_id(int(key_level_id))
        card_id = ekl.card.key().id()
        ekl.delete()
        return webapp2.redirect_to('card-edit', card_id=card_id)