from flask_restful import Resource,abort
from users import users
from flask import request ,jsonify
from models.users import User
from extensions import db
from api.schemas.user import UserSchema


class UserList(Resource):

    def get(self):
        users = User.query.all()
        schema = UserSchema(many=True)
        return {"results":schema.dump(users)}
    
    def post(self):
        data = request.json

        user = User(
            name=data.get("name"),
            age=data.get("age"),
            email=data.get("email"),
        )
        db.session.add(user)
        db.session.commit()
        
        # last_user_id = users[-1].get("id")
        # new_user = {"id":last_user_id+1,**data}
        # users.append(new_user)

        return jsonify(msg="User Created",user=user)
    
class UserResource(Resource):
    def get(self,user_id):
        # user = next(filter(lambda u :u.get("id") == user_id,users),None)
        user = User.query.get_or_404(user_id)

        # if user is None:
        #     abort(404)

        # return {"user":user}
        return jsonify(user=user)
    
    def put(self,user_id):
        data = request.json
        user = User.query.get_or_404(user_id)
        user.age = data.get("age")
        user.name = data.get("name")

        db.session.commit()

        return jsonify(msg="User updated",user=user)

        # user = None

        # for i ,u in enumerate(users):
        #     if u.get("id") == user_id:
        #         users[i] = {**u,**data} #**data will overdie the **u
        #         user = users[i]

        # if user is None:
        #     abort(404)

        # return {"msg":"User is updated","user":user}
        

    def delete(self,user_id):

        user = User.query.get_or_404(user_id)

        db.session.delete(user)

        return jsonify(mes = "User deleted")
        # user = None
        # for i ,u in enumerate(users):
        #     if u.get("id") == user_id:
        #         user = u
        #         users.pop(i)

        # if user is None:
        #     abort(404)

        # return {"msg":"User deleted"}

