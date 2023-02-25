from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        res = UserSchema(many=True).dump(all_users)
        return res, 200

    def post(self):
        data = request.json
        user = user_service.create(data)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:rid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        user_data = UserSchema().dump(user)
        return user_data, 200

    def put(self, uid):
        data = request.json
        if "id" not in data:
            data["id"] = uid

        user_service.update(data)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
