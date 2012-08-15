import webapp2

from utils.jinja_env import JinjaEnv
from models.text_line import TextLine

class TextLineHandler(webapp2.RequestHandler):
    def add_form(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/text_line_add_form.html')
            self.response.out.write(template.render({'card_id': card_id}))
    
    def add(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            TextLine.create(self.request.get('name'), int(card_id))
            return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def edit_form(self, text_line_id):
        text_line = TextLine.find_by_id(int(text_line_id))
        if text_line.card.is_authorized():
            template = JinjaEnv.get().get_template('templates/text_line_edit_form.html')
            self.response.out.write(template.render({'text_line_id': text_line_id, 'text_line': text_line}))
        
    def edit(self, text_line_id):
        text_line = TextLine.find_by_id(int(text_line_id))
        if text_line.card.is_authorized():
            text_line.name = self.request.get('name')
            text_line.save()
            return webapp2.redirect_to('card-edit', card_id=text_line.card.key().id())
    
    def delete_form(self, text_line_id):
        template = JinjaEnv.get().get_template('templates/text_line_delete_form.html')
        self.response.out.write(template.render({'text_line_id': text_line_id, 'text_line': text_line}))
        
    def delete(self, text_line_id):
        text_line = TextLine.find_by_id(int(text_line_id))
        if text_line.card.is_authorized():
            card_id = text_line.card.key().id()
            text_line.delete()
            return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def move_down(self, text_line_id):
        text_line = TextLine.find_by_id(int(text_line_id))
        if text_line.card.is_authorized(): 
            all_lines = text_line.card.text_lines()
            id_list = map(lambda x: x.key().id(), all_lines)
            index = id_list.index(text_line.key().id())
            if index < len(all_lines)-1:
                temp = text_line.position
                text_line.position = all_lines[index+1].position
                all_lines[index+1].position = temp
                text_line.save()
                all_lines[index+1].save()
            return webapp2.redirect_to('card-edit', card_id=text_line.card.key().id())  
    
    def move_up(self, text_line_id):
        text_line = TextLine.find_by_id(int(text_line_id))
        if text_line.card.is_authorized():
            all_lines = text_line.card.text_lines()
            id_list = map(lambda x: x.key().id(), all_lines)
            index = id_list.index(text_line.key().id())
            if index >= 1:
                temp = text_line.position
                text_line.position = all_lines[index-1].position
                all_lines[index-1].position = temp
                text_line.save()
                all_lines[index-1].save()
            return webapp2.redirect_to('card-edit', card_id=text_line.card.key().id())