from flask_restful import Resource,reqparse
from models.user import UserModel

class RegisterUser(Resource):


    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type = str,
        required = True,
        help = "This field is necessary"
        )
    parser.add_argument(
        "password",
        type = str,
        required = True,
        help = "This field is necessary"
        )

    def post(self):

        data = self.parser.parse_args()

        if UserModel.findByUsername(data["username"]):
            return {"message":"User already exists"},404
        
        user = UserModel(**data)
        user.insert()
        

        return {"message":"user registred"},201
        


    

    
            
