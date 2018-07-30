# -*- coding: utf-8 -*-

from mongoengine import (
    connect,
    Document,
    StringField,
    IntField,
    DecimalField
)
from mongoengine.context_managers import (
    switch_collection
)

import pymongo

connection = connect(db='moen', alias='moen')
connection_2 = connect(db='test', alias='test')


class Student(Document):

    name = StringField(min_length=5)
    age = IntField()

    meta = {'db_alias': 'test'}


if __name__ == '__main__':
    with switch_collection(Student, 'test') as Student:
        stu = Student.objects(name='not age').first()
        print(stu.name)
        print(stu.age)
    # client = pymongo.MongoClient()
    # print(client.list_database_names())
    # db = client['moen']
    # print(dir)


