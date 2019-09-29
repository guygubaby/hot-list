## Hot List `python version`

### 热榜是一个获取各大热门网站热门头条的聚合网站，使用python语言编写，多进程快速抓取信息

> 这个项目灵感来自于 [tophubs/TopList](https://github.com/tophubs/TopList) `golang version`

- flask
- mongodb
- docker


#### setup
```bash
./setup.sh
./bootstrap.sh
```

- 将会启动`4`个服务

     service | port | remark
     -----|------|-----
     server | 5000 | flask 服务(目前只做了`知乎`和`虎扑`)
     mongodb | 27017 | mongo数据库
     mongo-express | 8081 | 管理Mongodb
     web | 8080 | 前端(还在开发)
     
    
#### api 

- types
```
curl http://106.54.115.166:5000/api/types
```

```json
{
    "code": 0,
    "data": [
        {
        "id": 1,
        "title": "知乎"
        },
        {
        "id": 2,
        "title": "虎扑"
        }
    ]
}
```

- list
```bash
curl http://106.54.115.166:5000/api/list
# 支持添加从上一个接口拿到的 cate = {id} 参数
# curl http://106.54.115.166:5000/api/list?cate=1
```

```json
{
    "code": 0,
    "data": [
        {
        "_id": "5d8f2ad840d1afb2ab54ddf4",
        "cate": 1,
        "desc": "Android 现在上到 12GB 内存（RAM）了，是 iPhone6s 的 6 倍，苹果如果上 8GB 那不是一点都不会卡？还是这样慢慢升级让大家买新的？防止用户万年不换机？ iPhone 提升内存是否会进一步提升其易用性？如果会，那么 iPhone 为什么不加大内存？",
        "title": "iPhone 为什么不加大内存？",
        "url": "https://www.zhihu.com/question/276578129"
        }
    ]
}
```
