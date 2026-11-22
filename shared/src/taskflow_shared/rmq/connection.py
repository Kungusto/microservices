import aio_pika
from aio_pika.abc import AbstractRobustConnection
from taskflow_shared.config import settings

connection: None | AbstractRobustConnection = None


async def connect() -> None:
    global connection

    connection = await aio_pika.connect_robust(url=settings.RMQ_URL)


async def disconnect() -> None:
    global connection

    if connection and not connection.is_closed:
        await connection.close()

    connection = None


def get_rmq_conn() -> AbstractRobustConnection:
    if connection is None or connection.is_closed:
        raise ValueError("RabbitMQ connection hadn't been initialized")
    return connection
