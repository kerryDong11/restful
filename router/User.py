# encoding:UTF-8 
from flask_restful import Resource
from flask import Flask, jsonify, abort, request
from models.user import User as UserModel
#from models.user import UserModel
from models.db import db


class User(Resource):
    def get(self, user_id):
        print (user_id)
        user = UserModel.query.filter_by(username=user_id).first()
        if user:

            return user.to_dict()
        return {'message': 'User not found'}, 404

    # def get(self,user_id):
    #     return ''



class UserList(Resource):
    def get(self):

        return {'users': [user.to_dict() for user in UserModel.query.all()]}
    
    def post(self):
           
        # 查询该国家是否存在于数据库中
<<<<<<< Updated upstream
            name = request.json['username']
            u_id =  request.json['u_id']
            #udata = request.get_json()
           
            user = UserModel(username = name,u_id = u_id)
=======
            user = UserModel().from_dict(request.json)
>>>>>>> Stashed changes
            print(user)
            db.session.add(user)
            db.session.commit()
