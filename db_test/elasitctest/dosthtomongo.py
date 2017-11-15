# -*- coding: utf-8 -*-
from datetime import datetime
from pymongo import MongoClient, bulk

client = MongoClient('localhost', 27017)
db = client['local']
collection = db.test_collection


class OrderTable(object):

    @staticmethod
    def insert(shop_id: int,
               package_id: int,
               user_location: 'user gps data',
               created_at: datetime) -> bulk.ObjectId:

        """
        :return: created mongo order id
        """
        return collection.posts.insert_one(locals()).inserted_id


if __name__ == '__main__':
    now = datetime.now()
    id = OrderTable.insert(123, 1, [111, 222], now)
    print(id)
    print(type(id))
