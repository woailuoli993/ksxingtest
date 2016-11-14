# -*- coding:utf-8 -*-
# use python3
import operator


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))  # 两种排序方法   这种比较magic
    print(sorted(users, key=operator.attrgetter('user_id')))  # 这种比较快


if __name__ == '__main__':
    sort_notcompare()
