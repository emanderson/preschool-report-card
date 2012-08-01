from google.appengine.ext import db

class BaseModel(db.Model):
    @classmethod
    def report_key(self):
        db.Key.from_path('ReportCard', 'default_report_card')

    @classmethod
    def list(self):
        # TODO: handle larger sets
        return self.all().fetch(1000)

    @classmethod
    def find_by_id(self, id):
        return self.get_by_id(id, self.report_key())
