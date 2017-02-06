#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 22/01/2017
import threading
import platform
import time
import logging
from Queue import Queue
from random import randint

__doc__ = """ 抄董伟明,官方文档，廖雪峰 bogo  。。。。 threading 实验结果记录

"""

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) |||| %(message)s',)


def timeit(func):
    """一个简单的函数时间装饰器"""
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('{} COST: {}'.format(func.__name__, end-start))
    return wrapper


def show_thread_itself(arg):
    print("threading {} is running! ".format(threading.current_thread().getName()))

    for i in xrange(5):
        print('Thread {} >>> {}'.format(threading.current_thread().getName(), i))
        time.sleep(1)

    print("Thread {} end".format(threading.current_thread().getName()))

    pass


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


@timeit
def nothread():
    fib(34)
    fib(34)


@timeit
def withthread():
    for i in xrange(2):
        t = threading.Thread(target=fib, args=(34,))
        t.start()

    main_thread = threading.current_thread()

    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()


balance = 1000
lock = threading.Lock()


def change_balance():
    global balance
    balance += 1000
    balance -= 1000


def money_laundering(num):
    for i in xrange(num):
        change_balance()


def money_laundering_priveate(num):
    for i in xrange(num):
        lock.acquire()
        try:
            change_balance()
        finally:
            lock.release()


def lock_is_important():
    """
    这里的lock是一种互斥的 可重获的 锁 在一个加锁thread进行完之后将会释放。
    lock 相当于信号量（Sempahore） 为 1
    """
    @timeit
    def test1():
        print('Before i go to bank ,I have {}'.format(balance))
        t1 = threading.Thread(target=money_laundering, args=(2000000,))
        t2 = threading.Thread(target=money_laundering, args=(4000000,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("after two public_money_laundering, I have {}".format(balance))

    @timeit
    def test2():
        global balance
        balance = 2000
        print('Before i go to a new bank ,I have {}'.format(balance))
        t3 = threading.Thread(target=money_laundering_priveate, args=(3000000,))
        t4 = threading.Thread(target=money_laundering_priveate, args=(3000000,))
        t3.start()
        t4.start()
        t3.join()
        t4.join()
        print("after two private money_launderingm I have {}".format(balance))

    test1()
    test2()


def consumer_producer():
    condition = threading.Condition()

    def consumer(cond):

        t = threading.current_thread()
        print('{} start , and waiting for proc'.format(t.name))

        with cond:
            cond.wait()
            print('{} making resource avaiable to consumer'.format(t.name))

    def producer(cond):
        t = threading.current_thread()

        with cond:
            print('{} producer acaiable !'.format(t.name))
            cond.notifyAll() # 激活条件

    c1 = threading.Thread(name='cons1', target=consumer, args=(condition,))
    c2 = threading.Thread(name='cons2', target=consumer, args=(condition,))
    p = threading.Thread(name='prod', target=producer, args=(condition,))
    c1.start()
    time.sleep(1)
    c2.start()
    time.sleep(1)
    p.start()


def consumber_producer_event():
    """一个线程发送事件，其他的线程等待事件的触发  生产者消费者模型"""
    from random import randint

    TIMEOUT = 2
    eve = threading.Event()
    ll = []
    threads = []

    def consumer(event, l):
        """消费者"""
        mt = threading.currentThread()
        while 1:
            event_is_set = event.wait(TIMEOUT)
            if event_is_set:
                try:
                    integer = l.pop()
                    print('{} pop from list by {}'.format(integer, mt.name))
                    event.clear()  # 重制事件状态
                except IndexError:
                    pass  # 刚启动时容错。

    def producer(event, l):
        mt = threading.currentThread()
        while 1:
            integer = randint(10, 100)
            l.append(integer)
            print('{} is append to list by {}'.format(integer, mt.name))
            event.set()
            time.sleep(1)

        pass

    for name in ('consumer1', 'consumer2'):
        t = threading.Thread(name=name, target=consumer, args=(eve, ll))
        t.start()
        threads.append(t)

    p = threading.Thread(name='producer', target=producer, args=(eve, ll))
    p.start()
    threads.append(p)
    for t in threads:
        t.join()

    pass


def consumer_producer_queue():
    """ 有两种模式 priority 优先级模式 LIFOqueue后进先出模式。"""
    # priority 模式
    from random import random
    from Queue import PriorityQueue, LifoQueue

    q = PriorityQueue()

    def double(num):
        return num * 2

    def producer():
        while 1:
            wt = random()
            time.sleep(1)
            print('put', wt)
            q.put((double, wt))

    def consumer():
        while 1:
            task, arg = q.get()
            print arg, task(arg)
            q.task_done()

    for target in (producer, consumer):
        t = threading.Thread(target=target)
        t.start()


def consumer_producer_priqueue():
    """priority 优先级队列"""
    from random import randint
    from Queue import PriorityQueue

    pri_q = PriorityQueue()

    def triple(n):
        return n * 3

    def consumer():
        while 1:
            if pri_q.empty():
                break
            pri, target, arg = pri_q.get()
            print('[PRI: {}], {} * 3 = {}'.format(pri, arg, target(arg)))
            pri_q.task_done()
            time.sleep(1)

        pass

    def producer():
        count = 0
        while 1:
            if count > 50:
                break
            pri = randint(10, 100)
            print('put priority {} '.format(pri))
            pri_q.put((pri, triple, pri))
            count += 1
        pass

    for targ in (producer, consumer):
        t = threading.Thread(target=targ)
        t.start()
        time.sleep(1)


def daemon_and_not_daemon():

    def nd():
        logging.debug("start!")
        time.sleep(6)
        logging.debug("end!")

    def d():
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")

    t = threading.Thread(target=d, name="deamon")
    nt = threading.Thread(target=nd, name='no-deamon')
    t.setDaemon(True)
    t.start()

    nt.start()
    # 论join 的重要性。
    t.join()


# threading pool && threading module programing
def quadra(strings):
    return str(strings) * 4


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self._q = queue
        self.daemon = True
        self.start()

    def run(self):
        while 1:
            f, args, kwargs = self._q.get()

            try:
                print('USE {} '.format(self.name))
                print(f(*args, **kwargs))
            except Exception as e:
                print e
            self._q.task_done()
    pass


class ThreadingPool(object):

    def __init__(self, num_con=5):
        self._q = Queue(num_con)
        for _ in xrange(num_con):
            Worker(self._q)

    def add_task(self, f, *args, **kwargs):
        self._q.put((f, args, kwargs))

    def wait_complete(self):
        self._q.join()
    pass


def test_threading_pool():
    pool = ThreadingPool(10)
    for _ in xrange(1000):
        wt = randint(1, 9)
        pool.add_task(quadra, wt)
        time.sleep(1)
    pool.wait_complete()



def main():
    # nothread()
    # withthread(）
    # ----------------- no threading vs use treading-------------------------
    # show_thread_itself('no muti')
    # print('threading is running! thraead name is {}'.format(threading.current_thread().getName()))
    # t = threading.Thread(target=show_thread_itself, args=(123,), name='Do yourself')
    # t.start()
    # t.join()
    # print('threading {} end.'.format(threading.current_thread().getName()))
    # ------------------ problem on thread lock ---------------------------
    # lock_is_important()
    # ------------------ cunsumer / producter model with condition -----------------------
    # consumer_producer()
    # ------------------ cumsumer/ producter model with event -----------------
    # consumber_producer_event()
    # --------   deamon and not deamon threading   ------------------------
    # daemon_and_not_daemon()
    # ------------------ cunsumer / producter model with Queue -----------------------
    # consumer_producer_queue() # 普通队列
    # consumer_producer_priqueue()  # 优先级队列
    # ------------------ threadingpool ------------
    test_threading_pool()

    pass

if __name__ == '__main__':
    print("python version is {}".format(platform.python_version()))
    main()
    print("done!")
