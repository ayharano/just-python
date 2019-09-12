import asyncio


async def intervalo_progressivo(espera, até):
    for i in range(até):
        yield i
        await asyncio.sleep(espera)


async def async_set():
    return {
        valor
        async for valor in intervalo_progressivo(.001, 100)
        if valor % 2
    }


async def main():
    print(await async_set())


if __name__ == "__main__":
    # Python 3.7+
    asyncio.run(main())
