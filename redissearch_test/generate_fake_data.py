# -*- coding: utf-8 -*-
import sys

from redisearch import (
    Client,
    TextField
)
from bson import ObjectId
from redis import Redis, exceptions
from random import randint
import logging

__doc__ = """
    generate Faker redisearch index and documents.
"""

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)


def text_gen(lenth):

    with open('./seed_2.txt') as seed:

        for i in range(randint(200, 1000)):
            seed.readline()
        doc = ''
        while True:
            while len(doc) < lenth:
                doc += seed.readline().decode('utf-8')
            text, doc = doc[:lenth], doc[lenth:]
            lenth = yield text


_gen = text_gen(10)
_gen.send(None)


def gen_doc():
    return {
        'name': _gen.send(10),
        'description': _gen.send(100)
    }


if __name__ == '__main__':

    conn = Redis(host='192.168.57.22')
    volume = Client('volume', conn=conn)
    vm = Client('vm', conn=conn)

    volume_des = TextField('description')
    volume_name = TextField('name')
    # try:
    #     volume.drop_index()
    #     volume.create_index([volume_des, volume_name])
    # except exceptions.ResponseError:
    #     pass

    for i in range(400000):

        _id = str(ObjectId())
        doc = gen_doc()
        logging.debug("{0}, {1}, {2}".format(i, _id, doc))
        volume.add_document(_id, **doc)



