# -*- coding: utf-8 -*-

from mongoengine import (
    connect,
    Document,
    StringField,
    IntField,

)
from mongoengine.context_managers import (
    switch_collection
)

import pymongo

connection = connect(db='moen', alias='moen')
connection_2 = connect(db='test', alias='test')


class Student(Document):

    name = StringField()
    age = IntField()

    meta = {'db_alias': 'test'}


if __name__ == '__main__':
    # with switch_collection(Student, 'test') as Student:
    #     Student(name='yuhua', age='10101010').save()
    client = pymongo.MongoClient()
    print(client.list_database_names())
    db = client['moen']
    print(dir)


