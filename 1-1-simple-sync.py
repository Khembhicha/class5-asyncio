# import time.
import time

# suspend execution of the calling thread for however many seconds..
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    # delay 1 seconds.
    time.sleep(1)

# plus number : add loop numbers to make value until complete..
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name} : Computing {total} + {number}')
        sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n ')

# set time Start.
start = time.time()
# work value
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3])
]
# set time End.
end = time.time()
print(f'Time: {end-start:.2f} sec')