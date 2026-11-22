import asyncio

from icecream import ic
from taskflow_shared.rmq.connection import connect, disconnect, get_rmq_conn


async def listen_queue():
    connection = get_rmq_conn()
    async with connection.channel() as ch:
        queue = await ch.get_queue(name="task_queue")

        await ch.set_qos(prefetch_count=1)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    ic(message.body.decode())
                    await asyncio.sleep(5)


async def main():
    await connect()
    await listen_queue()
    await disconnect()


if __name__ == "__main__":
    asyncio.run(main())
