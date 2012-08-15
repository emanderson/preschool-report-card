import webapp2

from utils.jinja_env import JinjaEnv
from models.eval_item import EvalItem
from models.eval_category import EvalCategory

class ItemHandler(webapp2.RequestHandler):
    def add_form(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        if category.card.is_authorized():
            template = JinjaEnv.get().get_template('templates/item_add.html')
            self.response.out.write(template.render({'category_id': category_id}))
        
    def add(self, category_id):
        category = EvalCategory.find_by_id(int(category_id))
        if category.card.is_authorized():
            EvalItem.create(self.request.get('name'), int(category_id))
            return webapp2.redirect_to('card-edit', card_id=category.card.key().id(), _fragment="cat%sadd" % category_id)

    def edit_form(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/item_edit.html')
            self.response.out.write(template.render({'item_id': item_id, 'item': item}))
        
    def edit(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():            
            item.name = self.request.get('name')
            item.save()
            return webapp2.redirect_to('card-edit', card_id=item.category.card.key().id())

    def delete_form(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():            
            template = JinjaEnv.get().get_template('templates/item_delete.html')
            self.response.out.write(template.render({'item_id': item_id, 'item': item}))
        
    def delete(self, item_id):
        item = EvalItem.find_by_id(int(item_id))
        card = item.category.card
        if card.is_authorized():            
            card_id = item.category.card.key().id()
            item.delete()
            return webapp2.redirect_to('card-edit', card_id=card_id)

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