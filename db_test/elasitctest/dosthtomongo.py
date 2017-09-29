# _*_ coding:utf-8 _*_

from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient('localhost', 27017)

db = client.train
collection = db.protestcol
find = collection.find_one({'_id':ObjectId('5790330064325c1f57185e62')})
print find