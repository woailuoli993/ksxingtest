# _*_ coding:utf-8 _*_

import requests
import json


def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match": {
                "content": term
            }
        }
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results


def format_results(results):
    """Print results nicely:
    doc_id) content
    """
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s " % (doc['_id'], doc['_source']['content']))


def create_doc(uri, doc_data={}):
    """Create new document."""
    query = json.dumps(doc_data)
    print query
    response = requests.post(uri, data=query)
    print(response)


def config_elastic_river(conf_mongo_uri):
    """configure Elastic river to connect with mongo """
    doc_info = {
        "type": "mongodb",
        "mongodb": {
            "servers": [
                {"host": "127.0.0.1", "port": 27017}
            ],
            "db": "train",
            "colletion": "protestcol"
        },
        "index": {
            "name": "spiderindex",
            "type": "huaindex"
        }
    }
    doc_info = json.dumps(doc_info)
    print doc_info
    print conf_mongo_uri
    response = requests.put(conf_mongo_uri,doc_info)
    result  = json.loads(response.text)
    print '-----------', result


def getinfo_from_elk(url):
    """see sth like conf status...."""
    response = requests.get(url)
    result = json.loads(response.text)
    print result


if __name__ == '__main__':
    # url_search = 'http://localhost:9200/test/articles/_search'
    # url_create = 'http://localhost:9200/test/articles/'
    # url_conf_river = 'http://localhost:9200/_river/mongodb/_meta'
    # getqueryurl = 'http://localhost:9200/train/protestcol/_search?pretty=true'

    # for i in range(1, 100):
    #     data = "fox " + str(i)
    #     create_doc(url_create, {"content": data})
    # results = search(url_search, "fox")
    #  format_results(results)
    # config_elastic_river(url_conf_river)
    # getinfo_from_elk(getqueryurl)


