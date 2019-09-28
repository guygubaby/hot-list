from flask import Flask, request
from controller.hot_list import get_list
from spiders.bootstrap import bootstrap
from models.HotListResponse import HotListResponse
from utils.cates import all_category

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return HotListResponse.ok(data='pong')


@app.route('/api/types')
def get_types():
    return HotListResponse.ok(data=all_category)


@app.route('/api/list')
def get_hot_list():
    args = request.args
    _list = get_list(args)
    return HotListResponse.ok(data=_list)


bootstrap()

if __name__ == '__main__':
    app.run()
