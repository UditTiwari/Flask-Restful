from flask_restful import Resource,abort
from users import users
from flask import request


class UserList(Resource):

    def get(self):
        return {"result":users}
    
    def post(self):
        data = request.json
        last_user_id = users[-1].get("id")
        new_user = {"id":last_user_id+1,**data}
        users.append(new_user)

        return {"msg":"User Created","user":new_user}
    
class UserResource(Resource):
    def get(self,user_id):
        user = next(filter(lambda u :u.get("id") == user_id,users),None)

        if user is None:
            abort(404)

        return {"user":user}
    
    def put(self,user_id):
        data = request.json

        user = None

        for i ,u in enumerate(users):
            if u.get("id") == user_id:
                users[i] = {**u,**data} #**data will overdie the **u
                user = users[i]

        if user is None:
            abort(404)

        return {"msg":"User is updated","user":user}
        

    def delete(self,user_id):
        user = None
        for i ,u in enumerate(users):
            if u.get("id") == user_id:
                user = u
                users.pop(i)

        if user is None:
            abort(404)

        return {"msg":"User deleted"}

