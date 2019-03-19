import asyncio
import random
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

async def run(loop):
    nc = NATS()

    await nc.connect("localhost:4222", loop=loop)
    while True:
        await nc.publish("tenant1.clientPublish.topic1",int.to_bytes(random.randint(0,10000),length=4,byteorder="little"))
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(run(loop))