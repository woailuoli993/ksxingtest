import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(user='postgres',
                                 password="kingsoft",
                                 host="192.168.223.61",
                                 port="25432",
                                 database="postgres")

    values = await conn.fetch('''SELECT * FROM urls LIMIT 5;''')
    await conn.close()
    print(values)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())