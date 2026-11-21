import asyncio

from icecream import ic
from taskflow_shared import settings


async def main():
    ic(settings.RMQ_URL)

if __name__ == '__main__':
    asyncio.run(main())