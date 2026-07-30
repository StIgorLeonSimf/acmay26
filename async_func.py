from time import sleep, time
import asyncio

async def f1(x):
    print(x * 100)
    await asyncio.sleep(3)
    print('F1 completed')


async def f2(x):
    print(x / 10)
    await asyncio.sleep(2)
    print('F2 completed')


async def main():
    # task1 = asyncio.create_task(f1(4))
    # task2 = asyncio.create_task(f2(40))
    # await task1
    # await task2
    await asyncio.gather(f1(4), f2(40))



if __name__ == '__main__':
    start = time()
    asyncio.run(main())
    stop = time()
    print(f'Время выполнения: {stop - start:.2f}')
