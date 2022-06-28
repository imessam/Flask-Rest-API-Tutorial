from flask import Flask,jsonify,request
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import RegisterUser
from resources.item import Item,ItemList


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "hello"
api = Api(app)
jwt = JWT(app,authenticate,identity)

api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(RegisterUser,"/register")


if __name__ == "__main__":

    from db import db


    db.init_app(app)

    app.run(port = 5000)
