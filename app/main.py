import asyncio


async def handle_connection(reader, writer):
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break

            writer.write(b"+PONG\r\n")
            await writer.drain()
    except ConnectionError as err:
        print(err)
    finally:
        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        handle_connection,
        "localhost",
        6379,
    )

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
