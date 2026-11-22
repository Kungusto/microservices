import asyncio

from aio_pika import DeliveryMode, Message
from aio_pika.abc import AbstractRobustConnection
from faker import Faker
from taskflow_shared.rmq.connection import connect, disconnect, get_rmq_conn

faker = Faker("ru_RU")


async def publicate_message(connection: AbstractRobustConnection):
    async with connection.channel() as ch:
        for _ in range(100):
            await ch.default_exchange.publish(
                message=Message(
                    body=faker.sentence().encode(),
                    delivery_mode=DeliveryMode.PERSISTENT,
                ),
                routing_key="task_queue",
            )
            await asyncio.sleep(2)


async def main():
    await connect()
    connection = get_rmq_conn()
    await publicate_message(connection=connection)
    await disconnect()


if __name__ == "__main__":
    asyncio.run(main())
