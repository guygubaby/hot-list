from flask_restful import Resource
from utils.mongo import hupu_db
from models.HotListResponse import HotListResponse


class Hupu(Resource):
    def get(self):
        _list = hupu_db.find()
        res = []
        for item in _list:
            item['_id'] = str(item['_id'])
            res.append(item)
        return HotListResponse.ok(message=res)
