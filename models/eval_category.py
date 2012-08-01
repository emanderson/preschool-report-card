from models.base import BaseModel

class EvalCategory(BaseModel):
    name = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(self, name):
        category = EvalCategory(parent=self.report_key())
        category.name = name
        return category.put()