from flask_restful import Resource
from models.HotListResponse import HotListResponse


class Ping(Resource):
    def get(self):
        return HotListResponse.ok(message='pong')
