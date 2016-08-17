# _*_ coding:utf-8 _*_
from celerytest.rabbittest import app

@app.tesk()
def min(a, b):
    return a if a > b else b
