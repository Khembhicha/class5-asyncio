# import asyncio and time.
import asyncio
import time

# build hello function : sent output as started and done time.
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    # delay 4 seconds.
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# build main and build 2 tasks.
async def main():
    task1 = asyncio.create_task(hello(1)) # returns immediately,  the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    # delay task1.
    await task1
    # delay task2.
    await task2

if __name__ == '__main__':
    # set time Start.
    start = time.time()
    # run main function.
    asyncio.run(main())
    # set time End.
    end = time.time()
    print(f'Time: {end-start:.2f} sec')