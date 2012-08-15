import webapp2

from utils.jinja_env import JinjaEnv
from models.signature import Signature

class SignatureHandler(webapp2.RequestHandler):
    def add_form(self, card_id):
        template = JinjaEnv.get().get_template('templates/signature_add_form.html')
        self.response.out.write(template.render({'card_id': card_id}))
    
    def add(self, card_id):
        Signature.create(self.request.get('name'), int(card_id))
        return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def edit_form(self, signature_id):
        template = JinjaEnv.get().get_template('templates/signature_edit_form.html')
        self.response.out.write(template.render({'signature_id': signature_id, 'signature': Signature.find_by_id(int(signature_id))}))
        
    def edit(self, signature_id):
        tl = Signature.find_by_id(int(signature_id))
        tl.name = self.request.get('name')
        tl.save()
        return webapp2.redirect_to('card-edit', card_id=tl.card.key().id())
    
    def delete_form(self, signature_id):
        template = JinjaEnv.get().get_template('templates/signature_delete_form.html')
        self.response.out.write(template.render({'signature_id': signature_id, 'signature': Signature.find_by_id(int(signature_id))}))
        
    def delete(self, signature_id):
        tl = Signature.find_by_id(int(signature_id))
        card_id = tl.card.key().id()
        tl.delete()
        return webapp2.redirect_to('card-edit', card_id=card_id)
    
    def move_down(self, signature_id):
        tl = Signature.find_by_id(int(signature_id))
        all_sigs = tl.card.signatures()
        id_list = map(lambda x: x.key().id(), all_sigs)
        index = id_list.index(tl.key().id())
        if index < len(all_sigs)-1:
            temp = tl.position
            tl.position = all_sigs[index+1].position
            all_sigs[index+1].position = temp
            tl.save()
            all_sigs[index+1].save()
        return webapp2.redirect_to('card-edit', card_id=tl.card.key().id())  
    
    def move_up(self, signature_id):
        tl = Signature.find_by_id(int(signature_id))
        all_sigs = tl.card.signatures()
        id_list = map(lambda x: x.key().id(), all_sigs)
        index = id_list.index(tl.key().id())
        if index >= 1:
            temp = tl.position
            tl.position = all_sigs[index-1].position
            all_sigs[index-1].position = temp
            tl.save()
            all_sigs[index-1].save()
        return webapp2.redirect_to('card-edit', card_id=tl.card.key().id())