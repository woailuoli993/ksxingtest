# -*- coding: utf-8 -*-
import sys

import re
import time

import uuid

from pymongo import ASCENDING, TEXT
# from redisearch import (
#     Client,
#     TextField,
#     Query)
# from bson import ObjectId
# from redis import Redis, exceptions
# from random import randint
import logging
from pymongo.mongo_client import MongoClient

__doc__ = """
    generate Faker redisearch index and documents.
"""

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)


# def text_gen(lenth):
#
#     with open('./seed_2.txt') as seed:
#
#         for i in range(randint(200, 1000)):
#             seed.readline()
#         doc = ''
#         while True:
#             while len(doc) < lenth:
#                 doc += seed.readline().decode('utf-8')
#             text, doc = doc[:lenth], doc[lenth:]
#             lenth = yield text
#
#
# _gen = text_gen(10)
# _gen.send(None)
#
#
# def gen_doc():
#     return {
#         'name': _gen.send(10),
#         'description': _gen.send(20)
#     }

# def migrate():
#
#     conn = Redis(host='192.168.57.22')
#     volume = Client('volume', conn=conn)
#     volume_des = TextField('description')
#     volume_name = TextField('name')
#
#     try:
#         # volume.drop_index()
#         volume.create_index([volume_des, volume_name])
#     except exceptions.ResponseError:
#         pass
#
#     # for i in range(40000):
#
#     _id = str("12341234")
#     # doc = gen_doc()
#     # logging.debug("{0}, {1}, {2}".format(i, _id, doc))
#     volume.add_document(_id, language='chinese', name="vici test", description="嘻嘻 哈哈，")


def mongo_text_test():
    cli = MongoClient()
    test = cli.get_database("test").get_collection("test_search")
    test.create_index(
          [("super_type", ASCENDING), ("resource_state", ASCENDING),
           ("uuid", TEXT), ("name", TEXT), ("description", TEXT)],
          background=True
      )
    docs = [{
        "uuid": str(uuid.uuid4()),
        "name": str(i),
        "description": "Nature, \"time, and patience are "
        "the three great -physicians.",
        "super_type": "super_vol",
        "type": "vol",
        "create_time": int(
        time.time()),
        "resource_state": "inUse"
    } for i in range(1, 11)]
    test.insert_many(docs)

    text = [" -physicians"]
    print test.find({
                "description": {
                    "$regex":  "|".join([re.sub(
                        r"(\*|\.|\?|\+|\$|\^|\[|\]|\(|\)|\{|\}|\||\\|/)",
                        r"\\\1",
                        g
                    ) for g in text]),
                    "$options": "i"
                }
            }).count()


if __name__ == '__main__':
    # migrate()
    mongo_text_test()
    # conn = Redis(host='192.168.57.22')
    # volume = Client('volume_ch', conn=conn)
    # volume.search()
    # volume_des = TextField('description')
    # volume_name = TextField('name')
    #
    # docs = volume.search(Query('更加').summarize(['description']))
    #
    # for doc in docs.total:
    #     print(doc.id)
