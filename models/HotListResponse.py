class HotListResponse:
    def __init__(self):
        pass

    @staticmethod
    def ok(code=0, message='ok'):
        return {
            'code': code,
            'message': message
        }

    @staticmethod
    def error(code=-1, message='error'):
        return {
            'code': code,
            'message': message
        }
