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

    
# Normal function call
    start_time = time.time()
    api_worker("task-1")
    api_worker("task-2")
    end_time = time.time()
    print("Time taken by Normal function Call: {}".format(end_time - start_time))
    
# Using Multi Process
    start_time = time.time()
    
    proc1 = Process(target=api_worker, args=("task-1",))
    proc2 = Process(target=api_worker, args=("task-2",))
    
    proc1.start()
    proc2.start()
    
    proc1.join()
    proc2.join()
    
    end_time = time.time()
    
    print("Time taken by Multi process: {}".format(end_time - start_time))
    
# Using Multi Process - using Loop
    start_time = time.time()
    
    procs = []
    num_processes = multiprocessing.cpu_count()
    
    for i in range(num_processes):
        proc = Process(target=api_worker, args=("task-"+str(i),))
        procs.append(proc)
        proc.start()
        
    for proc in procs:
        proc.join()
    
    end_time = time.time()
    
    print("Time taken by Multi process using loop: {}".format(end_time - start_time))