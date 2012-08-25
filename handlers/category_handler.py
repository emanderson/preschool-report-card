import webapp2

from utils.jinja_env import JinjaEnv
from models.eval_category import EvalCategory
from models.report_card import ReportCard

class CategoryHandler(webapp2.RequestHandler):
    def add_form(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/category/add_form.html')
            self.response.out.write(template.render({'card_id': card_id}))
    
    def add(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            category_id = EvalCategory.create(self.request.get('name'), int(card_id)).id()
            category = EvalCategory.find_by_id(category_id)
            template = JinjaEnv.get().get_template('templates/category/edit_table.html')
            self.response.out.write(template.render({'category': category}))
    
    def edit_form(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        card = category.card
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/category/edit_form.html')
            self.response.out.write(template.render({'category_id': category_id, 'category': category}))
        
    def edit(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        card = category.card
        if card.is_authorized():
            category.name = self.request.get('name')
            category.save()
            return webapp2.redirect_to('card-edit', card_id=category.card.key().id())
    
    def delete_form(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        card = category.card
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/category/delete_form.html')
            self.response.out.write(template.render({'category_id': category_id, 'category': category}))
        
    def delete(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        card = category.card
        if card.is_authorized():
            category = EvalCategory.find_by_id(int(category_id))
            card_id = category.card.key().id()
            category.delete()
            return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def move_down(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        card = category.card
        if card.is_authorized():
            all_categories = category.card.categories()
            id_list = map(lambda x: x.key().id(), all_categories)
            index = id_list.index(category.key().id())
            if index < len(all_categories)-1:
                temp = category.position
                category.position = all_categories[index+1].position
                all_categories[index+1].position = temp
                category.save()
                all_categories[index+1].save()
            return webapp2.redirect_to('card-edit', card_id=category.card.key().id())  
    
    def move_up(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        card = category.card
        if card.is_authorized():            
            all_categories = category.card.categories()
            id_list = map(lambda x: x.key().id(), all_categories)
            index = id_list.index(category.key().id())
            if index >= 1:
                temp = category.position
                category.position = all_categories[index-1].position
                all_categories[index-1].position = temp
                category.save()
                all_categories[index-1].save()
            return webapp2.redirect_to('card-edit', card_id=category.card.key().id())