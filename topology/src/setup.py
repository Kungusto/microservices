import aio_pika


async def main():
    connection = aio_pika.connect_robust(
        url=""
    )

if __name__ == '__main__':
    main()