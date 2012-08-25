import webapp2

from utils.jinja_env import JinjaEnv
from models.signature import Signature
from models.report_card import ReportCard

class SignatureHandler(webapp2.RequestHandler):
    def add_form(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            template = JinjaEnv.get().get_template('templates/signature/add_form.html')
            self.response.out.write(template.render({'card_id': card_id}))
    
    def add(self, card_id):
        card = ReportCard.find_by_id(int(card_id))
        if card.is_authorized():
            signature_id = Signature.create(self.request.get('name'), int(card_id)).id()
            signature = Signature.find_by_id(signature_id)
            template = JinjaEnv.get().get_template('templates/signature/edit_row.html')
            self.response.out.write(template.render({'signature': signature}))
    
    def edit_form(self, signature_id):
        sig = Signature.find_by_id(int(signature_id))
        if sig.card.is_authorized():
            template = JinjaEnv.get().get_template('templates/signature/edit_form.html')
            self.response.out.write(template.render({'signature_id': signature_id, 'signature': sig}))
        
    def edit(self, signature_id):
        sig = Signature.find_by_id(int(signature_id))
        if sig.card.is_authorized():
            sig.name = self.request.get('name')
            sig.save()
            return webapp2.redirect_to('card-edit', card_id=sig.card.key().id())
    
    def delete_form(self, signature_id):
        sig = Signature.find_by_id(int(signature_id))
        if sig.card.is_authorized():
            template = JinjaEnv.get().get_template('templates/signature/delete_form.html')
            self.response.out.write(template.render({'signature_id': signature_id, 'signature': sig}))
        
    def delete(self, signature_id):
        sig = Signature.find_by_id(int(signature_id))
        if sig.card.is_authorized():
            card_id = sig.card.key().id()
            sig.delete()
            return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def move_down(self, signature_id):
        sig = Signature.find_by_id(int(signature_id))
        if sig.card.is_authorized():
            all_sigs = sig.card.signatures()
            id_list = map(lambda x: x.key().id(), all_sigs)
            index = id_list.index(sig.key().id())
            if index < len(all_sigs)-1:
                temp = sig.position
                sig.position = all_sigs[index+1].position
                all_sigs[index+1].position = temp
                sig.save()
                all_sigs[index+1].save()
            return webapp2.redirect_to('card-edit', card_id=sig.card.key().id())  
    
    def move_up(self, signature_id):
        sig = Signature.find_by_id(int(signature_id))
        if sig.card.is_authorized():
            all_sigs = sig.card.signatures()
            id_list = map(lambda x: x.key().id(), all_sigs)
            index = id_list.index(sig.key().id())
            if index >= 1:
                temp = sig.position
                sig.position = all_sigs[index-1].position
                all_sigs[index-1].position = temp
                sig.save()
                all_sigs[index-1].save()
            return webapp2.redirect_to('card-edit', card_id=sig.card.key().id())