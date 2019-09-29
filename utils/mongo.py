from pymongo import MongoClient
import config

client = MongoClient(config.MONGO_DEV_URL,config.MONGO_DEV_PORT,connect=False)

db = client.hotlist

hot_collection = db.list


