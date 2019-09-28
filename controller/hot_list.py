from utils.mongo import hot_collection


def get_list(args):
    res = []
    cate = args.get('cate', 1)
    _list = hot_collection.find({'cate': int(cate)})
    for item in _list:
        item['_id'] = str(item['_id'])
        res.append(item)
    return res
