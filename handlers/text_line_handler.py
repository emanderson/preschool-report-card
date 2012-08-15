import webapp2

from utils.jinja_env import JinjaEnv
from models.text_line import TextLine

class TextLineHandler(webapp2.RequestHandler):
    def add_form(self, card_id):
        template = JinjaEnv.get().get_template('templates/text_line_add_form.html')
        self.response.out.write(template.render({'card_id': card_id}))
    
    def add(self, card_id):
        TextLine.create(self.request.get('name'), int(card_id))
        return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def edit_form(self, text_line_id):
        template = JinjaEnv.get().get_template('templates/text_line_edit_form.html')
        self.response.out.write(template.render({'text_line_id': text_line_id, 'text_line': TextLine.find_by_id(int(text_line_id))}))
        
    def edit(self, text_line_id):
        tl = TextLine.find_by_id(int(text_line_id))
        tl.name = self.request.get('name')
        tl.save()
        return webapp2.redirect_to('card-edit', card_id=tl.card.key().id())
    
    def delete_form(self, text_line_id):
        template = JinjaEnv.get().get_template('templates/text_line_delete_form.html')
        self.response.out.write(template.render({'text_line_id': text_line_id, 'text_line': TextLine.find_by_id(int(text_line_id))}))
        
    def delete(self, text_line_id):
        tl = TextLine.find_by_id(int(text_line_id))
        card_id = tl.card.key().id()
        tl.delete()
        return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def move_down(self, text_line_id):
        tl = TextLine.find_by_id(int(text_line_id))
        all_lines = tl.card.text_lines()
        id_list = map(lambda x: x.key().id(), all_lines)
        index = id_list.index(tl.key().id())
        if index < len(all_lines)-1:
            temp = tl.position
            tl.position = all_lines[index+1].position
            all_lines[index+1].position = temp
            tl.save()
            all_lines[index+1].save()
        return webapp2.redirect_to('card-edit', card_id=tl.card.key().id())  
    
    def move_up(self, text_line_id):
        tl = TextLine.find_by_id(int(text_line_id))
        all_lines = tl.card.text_lines()
        id_list = map(lambda x: x.key().id(), all_lines)
        index = id_list.index(tl.key().id())
        if index >= 1:
            temp = tl.position
            tl.position = all_lines[index-1].position
            all_lines[index-1].position = temp
            tl.save()
            all_lines[index-1].save()
        return webapp2.redirect_to('card-edit', card_id=tl.card.key().id())