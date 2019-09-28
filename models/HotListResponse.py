from flask import jsonify


class HotListResponse:
    def __init__(self):
        pass

    @staticmethod
    def ok(code=0, data='ok'):
        return jsonify({
            'code': code,
            'data': data
        })

    @staticmethod
    def error(code=-1, data='error'):
        return jsonify({
            'code': code,
            'data': data
        })
