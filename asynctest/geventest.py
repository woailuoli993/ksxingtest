# -*- coding: utf-8 -*-

import gevent
from gevent import Timeout, pool
from gevent.monkey import patch_all
# from gevent.greenlet

# from smartx_app.elf.common.utils import timeout

patch_all()


def p(x):
    print x, "start"
    gevent.sleep(1)
    print x, "test mid."
    gevent.sleep(0.1)
    print x, "test done."


@timeout.timeout(1)
def run_p():

    new_pool = pool.Pool(20)
    try:
        timer = Timeout(3)
        timer.start()
        for _ in new_pool.imap(p, range(20), maxsize=2):
            pass
        gevent.sleep(0.1)
    except Exception:
        print("---------------- timeout")

    finally:
        print("kill")
        new_pool.kill()
        print("task done.")
        gevent.sleep(0.1)
        print("---------------------------5 later")
    return [1, 2, 3]


if __name__ == '__main__':
    print("start gevent")
    run_p()
    gevent.sleep(3)
    print("----------------------------done")
