from . import db

class Test(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    testfield = db.Column(db.String(80), nullable=False)

    def __init__(self, testfield):
        self.testfield = testfield


    def serialize(self):
        return {
            'id': self.id,
            'testfield': self.testfield,
        }
