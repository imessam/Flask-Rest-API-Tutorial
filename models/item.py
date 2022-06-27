from db import db


class ItemModel(db.Model):

    __tablename__ = "ITEMS"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))

    def __init__(self,name,price):
        self.name = name
        self.price = price

    @classmethod
    def findByName(cls,name):
        
        return cls.query.filter_by(name = name).first()

    def insert(self):

        db.session.add(self)
        db.session.commit()

    def json(self):

        return {"name":self.name,"price":self.price}

        

        
