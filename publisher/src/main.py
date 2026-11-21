import asyncio

from taskflow_shared import settings
from icecream import ic


async def main():
    ic(settings.RMQ_URL)

if __name__ == '__main__':
    asyncio.run(main())