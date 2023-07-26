# import time
import time

# suspend execution of the calling thread for however many seconds.
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# plus number
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name} : Computing {total} + {number}')
        sleep()
        total += number
    #
    print(f'Task {name}: Sum = {total}\n ')

# measure the total time elapsed to execute the script in seconds at Start.
start = time.time()
# work value
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3])
]
# measure the total time elapsed to execute the script in seconds at End.
end = time.time()
print(f'Time: {end-start:.2f} sec')