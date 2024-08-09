import threading
import time


def api_worker():
    while True:
        print(f"running..")
        time.sleep(1)


def execute_stuff():
    print("executed!")


# in this case execute_stuff never gets executed due to infinite loop in api_worker
# api_worker()
# execute_stuff()

thread1 = threading.Thread(target=api_worker)
thread1.start()

execute_stuff()
