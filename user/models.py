from pymongo import MongoClient
from dotenv import load_dotenv
import os
from rest_framework.exceptions import APIException
load_dotenv()

class NotFoundError(APIException):
    status_code = 404
    default_detail = "not found user"

client = MongoClient("localhost",27017)
db = client[os.getenv("DB_NAME")]

class User():
    @staticmethod
    def find():
        users = []
        for u in db.users.find():
            u.update({'_id': str(u["_id"])})
            users.append(u)
        return users

    @staticmethod
    def create(data: dict):
        db.users.insert_one(data)

    @staticmethod
    def update(id, data: dict):
        user = db.users.find_one({'_id': id})

        if not user:
            raise NotFoundError

        update = {"$set": data}
        res = db.users.find_one_and_update(user, update)
        res.update({'_id': str(res["_id"])})
        return res

    @staticmethod
    def delete(id):
        user = db.users.find_one({'_id': id})

        if not user:
            raise NotFoundError

        db.users.delete_one(user)
        return {"msg": "deleted sucess"}
