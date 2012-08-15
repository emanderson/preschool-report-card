import webapp2

from utils.jinja_env import JinjaEnv
from models.eval_category import EvalCategory

class CategoryHandler(webapp2.RequestHandler):
    def add_form(self, card_id):
        template = JinjaEnv.get().get_template('templates/category_add.html')
        self.response.out.write(template.render({'card_id': card_id}))
    
    def add(self, card_id):
        EvalCategory.create(self.request.get('name'), int(card_id))
        return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def edit_form(self, category_id):
        template = JinjaEnv.get().get_template('templates/category_edit_form.html')
        self.response.out.write(template.render({'category_id': category_id, 'category': EvalCategory.find_by_id(int(category_id))}))
        
    def edit(self, category_id):
        ec = EvalCategory.find_by_id(int(category_id))
        ec.name = self.request.get('name')
        ec.save()
        return webapp2.redirect_to('card-edit', card_id=ec.card.key().id())
    
    def delete_form(self, category_id):
        template = JinjaEnv.get().get_template('templates/category_delete_form.html')
        self.response.out.write(template.render({'category_id': category_id, 'category': EvalCategory.find_by_id(int(category_id))}))
        
    def delete(self, category_id):
        ec = EvalCategory.find_by_id(int(category_id))
        card_id = ec.card.key().id()
        ec.delete()
        return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def move_down(self, category_id):
        ec = EvalCategory.find_by_id(int(category_id))
        all_categories = ec.card.categories()
        id_list = map(lambda x: x.key().id(), all_categories)
        index = id_list.index(ec.key().id())
        if index < len(all_categories)-1:
            temp = ec.position
            ec.position = all_categories[index+1].position
            all_categories[index+1].position = temp
            ec.save()
            all_categories[index+1].save()
        return webapp2.redirect_to('card-edit', card_id=ec.card.key().id())  
    
    def move_up(self, category_id):
        ec = EvalCategory.find_by_id(int(category_id))
        all_categories = ec.card.categories()
        id_list = map(lambda x: x.key().id(), all_categories)
        index = id_list.index(ec.key().id())
        if index >= 1:
            temp = ec.position
            ec.position = all_categories[index-1].position
            all_categories[index-1].position = temp
            ec.save()
            all_categories[index-1].save()
        return webapp2.redirect_to('card-edit', card_id=ec.card.key().id())