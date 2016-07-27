from elasticsearch import Elasticsearch
from datetime import datetime

if __name__ == '__main__':
    print 'r'*30
    es = Elasticsearch({'host': '10.174.93.111', 'port': '9200'})
    es_one = es.get(index='ksxing', doc_type='testqm', id='5545c306f3805c7730c35fad')
    print "es_one:", es_one
