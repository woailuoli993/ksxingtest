#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 08/03/2017

import requests
import time
import collections
import itertools
import multiprocessing
import string


class SimpleMapReduce(object):
    def __init__(self, map_func, reduce_func, num_workers=10):
        """
        map_func

          Function to map inputs to intermediate data. Takes as
          argument one input value and returns a tuple with the key
          and a value to be reduced.

        reduce_func

          Function to reduce partitioned version of intermediate data
          to final output. Takes as argument a key as produced by
          map_func and a sequence of the values associated with that
          key.

        num_workers

          The number of workers to create in the pool. Defaults to the
          number of CPUs available on the current host.
        """
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)  # 创建进程池。

    def partition(self, mapped_values):
        """Organize the mapped values by their key.
        Returns an unsorted sequence of tuples with a key and a sequence of values.
        将获取到的进程map 结果进行整合。 并按其key值归类。
        """
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        """Process the inputs through the map and reduce functions given.

        inputs
          An iterable containing the input data to be processed.

        chunksize=1
          The portion of the input data to hand to each worker.  This
          can be used to tune performance during the mapping phase.
        """
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        return map_responses
        # partitioned_data = self.partition(itertools.chain(*map_responses))  # chain 整合 所有map 回调函数的结果。

        # reduced_values = self.pool.map(self.reduce_func, partitioned_data)



def file_to_words(filename):
    """Read a file and return a sequence of (word, occurances) values.
    """
    output = []
    with open('url.txt', 'r') as f:
        for line in f:

            r = requests.get('http://192.168.223.63/query?url={}'.format(line))

    return r.content


def count_words():
    pass

if __name__ == '__main__':

    import operator
    import glob

    input_files = 'url.txt'
    print(input_files)

    mapper = SimpleMapReduce(file_to_words, count_words, 1)  # 注入回调。
    word_counts = mapper(input_files)  # 添加要分析的文件
    print 1
    # word_counts.sort(key=operator.itemgetter(1), reverse=True)  # 按数量从大到小排。

    # print '\nTOP 20 WORDS BY FREQUENCY\n'
    # top20 = word_counts[:20]
    # longest = max(len(word) for word, count in top20)
    # for word, count in top20:
        # print '%-*s: %5s' % (longest + 1, word, count)




        # write = open("new.txt", 'wb+')


