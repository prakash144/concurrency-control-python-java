import threading
import time


def api_worker():
    print(f"executing CPU intensive worker...")
    total = 0
    for i in range(10000):
        for j in range(10000):
            total += i*j
    return total


print("----------------- Without Thread --------------")

start_time = time.time()

for _ in range(2):
    api_worker()

end_time = time.time()
print(f"Time Taken : {end_time - start_time} seconds")

print("------------------ With Thread ------------------")

start_time = time.time()

thread1 = threading.Thread(target=api_worker)
thread2 = threading.Thread(target=api_worker)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

end_time = time.time()
print(f"With Thread Time Taken : {end_time - start_time} seconds")
