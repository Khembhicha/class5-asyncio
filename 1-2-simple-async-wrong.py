# import asyncio and time
import asyncio
import time

# suspend execution of the calling thread for however many seconds.
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    # delay 1 seconds
    time.sleep(1)

# plus number : add loop numbers to make value until complete.
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'task {name}: Computing {total}+{number}')
        # call asyncronous await function for do another work while waiting sleep working
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

# set time Start.
start = time.time()
# build loop for get value.
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
# loop run until complete.
loop.run_until_complete(asyncio.wait(tasks))
# close the loop.
loop.close()
# set time End.
end = time.time()
print(f'Time: {end-start:.2f} sec')