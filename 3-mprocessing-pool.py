# Multiprocessing in Python
# Purpose: Enables concurrent execution of processes, which can take advantage of multiple CPU cores.
# Library: multiprocessing module.

# Key Concepts
# Process: Independent, separate memory space, and runs independently of other processes.
# Pool: Manages a pool of worker processes, useful for parallelizing tasks.

from multiprocessing import Process
import multiprocessing
import time


def api_worker(task: str):
    print("executing CPU intensive task ...: ", task.upper())
    total = 0
    for i in range(10000):
        for j in range(10000):
            total += i * j
    return {task: total}


if __name__ == "__main__":
    # In place of queue we can use pool for same
    start_time = time.time()

    num_process = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_process)

    result = pool.map(api_worker, ["task-1", "task-2"])
    pool.close()
    pool.join()

    end_time = time.time()
    print("Time taken using pool: {}".format(end_time - start_time))
    print(result)
