import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel




class Item(Resource):


    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type = str,
        required = True,
        help = "This field is necessary"
        )

    
    @jwt_required()
    def get(self,name):

        item = ItemModel.findByName(name)

        if item:
            return item.json(),200

        return {"message":"item not found"},404

    

    def post(self,name):

        item = ItemModel.findByName(name)
        if item:
            return {"message":f"Item of name {name} exists"},400 
        
        data = self.parser.parse_args()
        newItem = ItemModel(name,data["price"])

        newItem.insert()
        
        return newItem.json(),201

    

class ItemList(Resource):

    def get(self):
        return {"Items":[item.json() for item in ItemModel.query.all()]}
