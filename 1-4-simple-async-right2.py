# Class 1-4 simple-async-right2.py
import asyncio
import time

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task{name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

async def main():
    await asyncio.gater(sum("A", [1, 2]), sum("B", [1, 2, 3]))

if __name__ == '_main_':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time; {end-start:.2f} sec')