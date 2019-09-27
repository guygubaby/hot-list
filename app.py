from flask import Flask
from flask_restful import Api
from controller import *
from spiders.bootstrap import bootstrap

app = Flask(__name__)
api = Api(app)

api.add_resource(Ping, '/')
api.add_resource(ZhiHu, '/zhihu')
api.add_resource(Hupu, '/hupu')

bootstrap()

if __name__ == '__main__':
    app.run()
