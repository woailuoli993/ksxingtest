# _*_ coding:utf-8 _*_

import pika
from celery import Celery


# celery 相关配置  队列地址  结果存放地址 消息格式
CELERY_BROKER_URL = 'mongodb://10.174.93.111:27017/celery'
CELERY_RESULT_BACKEND = 'mongodb://10.174.93.111:27017/celery'
CELERY_TASK_SERIALIZER = 'json'

app = Celery(__name__, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    pass

# 神奇的config 技巧
# 1. 设置计算结果
CELERY_TASK_RESULT_EXPIRES = 3600

# 关于后台运行及日志的记录

