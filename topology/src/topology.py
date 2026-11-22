import aio_pika
from aio_pika import ExchangeType
from aio_pika.abc import AbstractRobustConnection
from icecream import ic


async def fill_up_rmq(connection: AbstractRobustConnection):
    async with connection.channel() as channel:
        email_queue = await channel.declare_queue(name="email_queue", durable=True)
        report_queue = await channel.declare_queue(name="report_queue", durable=True)
        email_exchange = await channel.declare_exchange(
            "email",
            ExchangeType.DIRECT,
            durable=True
        )
        report_exchange = await channel.declare_exchange(
            "report",
            ExchangeType.DIRECT,
            durable=True
        )
        await email_queue.bind(
            exchange=email_exchange,
            routing_key="email"
        )
        await report_queue.bind(
            exchange=report_exchange,
            routing_key="report"
        )

