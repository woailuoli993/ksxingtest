# -*- coding: utf-8 -*-
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('192.168.31.185', 27017)
db = client['vici_test']


def mulit_transaction():

    with client.start_session() as session:
        with session.start_transaction():
            print('[+] transaction start...')
            db.bankA.update_one({"account": "vici", "qty": {"$gte": 100}},
                                {"$inc": {"qty": -100}},
                                session=session)
            # vici = db.bankA.find_one({"account": "vici"}, session=session)
            vici = db.bankA.find_one({"account": "vici"})
            print('vici have {}'.format(vici['qty']))
            db.bankB.update_one({"account": "li"},
                                {"$inc": {"qty": 100}},
                                session=session)
            # li = db.bankB.find_one({"account": "li"}, session=session)
            li = db.bankB.find_one({"account": "li"})
            print('li have {}'.format(li['qty']))
            # assert 1 == 2


if __name__ == '__main__':
    # clean
    db.bankA.remove({})
    db.bankB.remove({})

    # fixture
    db.bankA.insert_one({"account": "vici", "qty": 1000})
    db.bankB.insert_one({"account": "li", "qty": 50})
    vici = db.bankA.find_one({"account": "vici"})
    li = db.bankB.find_one({"account": "li"})

    print('[+] ....\nvici account: \t{} \nli account: \t{}'.format(vici['qty'],
                                                                   li['qty']))

    mulit_transaction()
