# -*- coding: utf-8 -*-
import collections
import re


def wc(file, limit=None):
    """count word in file
    :param file: path of file
    :param limit: top n of cont list
    :return: list of word and count with size n
    """
    count_list = collections.Counter()
    with open(file) as f:
        for line in f:
            count_list.update(map(lambda x: x.lower(),
                                  re.findall(r'\w+', line)))
    limit = min(limit, len(count_list)) or len(count_list)
    row_format = "{:<15}{:<6}"
    print(row_format.format('word', 'count'))
    print(row_format.format('-'*14, '-'*5))
    for t in count_list.most_common(limit):
        print(row_format.format(*t))


def nc(n):
    """count of 0-9 in 1-N

    :param n: upper limit
    :return:
    """
    num_list = range(10)
    n_len = len(str(n))
    count_dict = {}

    def count(x):
        """count x in 1-n"""

        cont = 0
        for b in range(n_len):
            # high
            i = 10 ** b
            k = n / i
            h = k / 10
            if x == 0:
                if h:
                    h -= 1
                else:
                    break
            cont += h * i

            # current
            cur = k % 10
            if cur > x:
                cont += i
            elif cur == x:
                cont += n - k * i + 1
        count_dict[x] = cont

    map(count, num_list)
    row_format = "{:<4}{:<6}"
    print(row_format.format('num', 'count'))
    print(row_format.format('-'*3, '-'*5))
    for t in num_list:
        print(row_format.format(t, count_dict[t]))


def kc(number_list, k):
    num_set = set(number_list)
    count = 0
    while num_set:
        num_1 = num_set.pop()
        num_2 = k - num_1
        if num_2 in num_set:
            num_set.remove(num_2)
            count += 1
    print(count)


if __name__ == '__main__':

    q_1 = ('news.txt', 10)
    q_2 = 2593
    q_3 = ([11, 44, 22, 33, 55, 51, 4, 66], 55)

    # q_1
    print('question_1 with args:', q_1)
    wc(*q_1)
    # q_2
    print('question_2 with args:', q_2)
    nc(q_2)
    # q_3
    print('question_3 with args:', q_3)
    kc(*q_3)
