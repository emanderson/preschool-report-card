import webapp2

from utils.jinja_env import JinjaEnv
from models.eval_item import EvalItem
from models.eval_category import EvalCategory

class ItemHandler(webapp2.RequestHandler):
    def add_form(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        if category.card.is_authorized():
            template = JinjaEnv.get().get_template('templates/item/add_form.html')
            self.response.out.write(template.render({'category_id': category_id}))
        
    def add(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        if category.card.is_authorized():
            item_id = EvalItem.create(self.request.get('name'), int(category_id)).id()
            item = EvalItem.find_by_id(item_id)
            template = JinjaEnv.get().get_template('templates/item/edit_row.html')
            self.response.out.write(template.render({'item': item}))

    def edit_form(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/item/edit_form.html')
            self.response.out.write(template.render({'item_id': item_id, 'item': item}))
        
    def edit(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():            
            item.name = self.request.get('name')
            item.save()
            template = JinjaEnv.get().get_template('templates/item/edit_row.html')
            self.response.out.write(template.render({'item': item}))

    def delete_form(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():            
            template = JinjaEnv.get().get_template('templates/item/delete_form.html')
            self.response.out.write(template.render({'item_id': item_id, 'item': item}))
        
    def delete(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():            
            card_id = item.category.card.key().id()
            item.delete()

    def move_down(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():            
            all_items = item.category.items()
            id_list = map(lambda x: x.key().id(), all_items)
            index = id_list.index(item.key().id())
            if index < len(all_items)-1:
                temp = item.position
                item.position = all_items[index+1].position
                all_items[index+1].position = temp
                item.save()
                all_items[index+1].save()
            return webapp2.redirect_to('card-edit', card_id=item.category.card.key().id())

    def move_up(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():   
            all_items = item.category.items()
            id_list = map(lambda x: x.key().id(), all_items)
            index = id_list.index(item.key().id())
            if index >= 1:
                temp = item.position
                item.position = all_items[index-1].position
                all_items[index-1].position = temp
                item.save()
                all_items[index-1].save()
            return webapp2.redirect_to('card-edit', card_id=item.category.card.key().id())