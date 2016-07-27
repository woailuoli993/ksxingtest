# _*_ coding:utf-8 _*_

# mongo  副本集及初始化

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client.testdb

# print db
collection = db.testcol

import datetime
for i in range(1, 100):
    post = {
        "text": "天朝火车没有轨道",
        "date": datetime.datetime.utcnow()}

    collection.insert_one(post)






