# -*- coding: utf-8 -*-
import queue


class ObjPool:

    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
            return self.item

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.item is not None:
            self._queue.put(self.item)
            self. item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self. item = None


my_queue = queue.Queue(maxsize=20)

my_queue.put('huahua')
my_queue.put('dandan')


def do_sth_in_queue(myqueue):
    with ObjPool(myqueue) as obj:
        print(f'inside {obj}')
    out_item = myqueue.get()
    print(f'outside {out_item}')
    myqueue.put(out_item)
    while True:
        with ObjPool(myqueue) as obj:
            print(f'inside {obj}')


do_sth_in_queue(my_queue)
