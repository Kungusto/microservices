import asyncio

from src.topology import fill_up_rmq
from taskflow_shared.rmq.connection import connect, disconnect, get_rmq_conn


async def main():
    await connect()
    await fill_up_rmq(connection=get_rmq_conn())
    await disconnect()


if __name__ == "__main__":
    asyncio.run(main())
