import asyncio
import datetime

async def display_date(loop):
    end_time = loop.time() + 50000.0
    a = 1
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        b = await domywork(a)
        a += 1
        print(b)

async def domywork(a):
    await asyncio.sleep(1)
    return a

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.close()