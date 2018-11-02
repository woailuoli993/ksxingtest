# -*- coding: utf-8 -*-
from bson import ObjectId
from pymongo import MongoClient
import copy

client = MongoClient('localhost', 27017)
db = client['local']
collection = db.test_collection


# class OrderTable(object):
#
#     @staticmethod
#     def insert(shop_id: int,
#                package_id: int,
#                user_location: 'user gps data',
#                created_at: datetime) -> bulk.ObjectId:
#
#         """
#         :return: created mongo order id
#         """
#         return collection.posts.insert_one(locals()).inserted_id

def add_oid(doc):
    doc[u'_id'] = ObjectId()
    return doc


def scala_collection():
    client = MongoClient('192.168.31.185')
    resources = client['resources']
    resource = resources['resource']

    data = list(resource.find({"type": "KVM_VM"}, {'_id': False}))
    for i in range(2000):
        new_data = list(map(add_oid, copy.deepcopy(data)))
        with client.start_session() as session:
            session.start_transaction()
            resource.insert_many(new_data, session=session)
            print('session {} done'.format(i))
            session.commit_transaction()


if __name__ == '__main__':
    # now = datetime.now()
    # id = OrderTable.insert(123, 1, [111, 222], now)
    # print(id)
    # print(type(id))
    scala_collection()

    {"type": 'KVM_VM', 'status': "running", node_ip: "10.0.57.21"}
