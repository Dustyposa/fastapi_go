from asyncio import start_server, run


async def on_client_connected(reader, writer):
    while True:
        data = await reader.readline()
        if not data:
            break
        writer.write(data)


async def server():
    srv = await start_server(on_client_connected, '127.0.0.1', 8888)
    async with srv:
        await srv.serve_forever()


run(server())
