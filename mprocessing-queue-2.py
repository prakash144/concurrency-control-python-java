# Multiprocessing in Python
    # Purpose: Enables concurrent execution of processes, which can take advantage of multiple CPU cores.
    # Library: multiprocessing module.

# Key Concepts
    # Process: Independent, separate memory space, and runs independently of other processes.
    # Pool: Manages a pool of worker processes, useful for parallelizing tasks.
    
from multiprocessing import Process, Queue
import multiprocessing
import time

def api_worker(task: str, queue):
    print("executing CPU intensive task ...: ", task.upper())
    total = 0
    for i in range(10000):
        for j in range(10000):
            total += i * j
    return queue.put({task: total})

if __name__ == "__main__":

# Get worker value using queue or pipe here we have queue example
    que = Queue()
    start_time = time.time()
    
    proc1 = Process(target=api_worker, args=("task-1", que, ))
    proc2 = Process(target=api_worker, args=("task-2", que, ))
    
    proc1.start()
    proc2.start()
    
    proc1.join()
    proc2.join()
    
    end_time = time.time()
    
    print("Time taken by Multi process and get data using queue: {}".format(end_time - start_time))
    for _ in range(2):
        print(que.get())