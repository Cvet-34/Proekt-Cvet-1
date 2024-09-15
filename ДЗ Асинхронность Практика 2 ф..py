import time
import asyncio

async def start_strongman(name, power): # Старт
    print(f'Силач {name} начал соревнования.')
    await asyncio.sleep(5)


async def start_tournament(name, power):
    sila = 0
    while sila < power:
        print(f'{name} поднял {sila + 1} шар(ов)')
        f'{name}{await asyncio.sleep(power)}'
        f'{name}{await asyncio.sleep(power)}'
        f'{name}{await asyncio.sleep(power)}'
        sila += 1

    print(f'Силач {name} закончил соревнования')

async def main():
    print('Старт')
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))

    task12 = asyncio.create_task(start_tournament('Pasha', 3))

    task22 = asyncio.create_task(start_tournament('Denis', 4))

    task32 = asyncio.create_task(start_tournament('Apollon', 5))
    await task1
    await task2
    await task3
    await task12
    await task22
    await task32

    print('Соревнования окончены')


asyncio.run(main())
