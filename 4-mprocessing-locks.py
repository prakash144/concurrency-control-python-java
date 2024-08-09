import multiprocessing


class BankAccount:
    def __init__(self, balance):
        self.balance = multiprocessing.Value('i', balance)  # Use Value to share balance

    def deposit(self, amount):
        print(f"Depositing {amount}")
        self.balance.value += amount
        print(f"New balance after deposit: {self.balance.value}")


class BankAccountWithLock:
    def __init__(self, balance):
        self.balance = multiprocessing.Value('i', balance)  # Shared balance with multiprocessing.Value

    def deposit(self, amount, lock):
        # lock.acquire()
        with lock:  # Ensure thread safety with the lock
            print(f"Depositing {amount}")
            self.balance.value += amount
            print(f"New balance after deposit: {self.balance.value}")
        # lock.release()


if __name__ == "__main__":
    print("----------------Before Lock--------------------")
    account = BankAccount(balance=1000)

    # Simulate multiple transactions using processes
    processes = []
    process1 = multiprocessing.Process(target=account.deposit, args=(100,))
    process2 = multiprocessing.Process(target=account.deposit, args=(100,))

    processes.append(process1)
    processes.append(process2)

    process1.start()
    process2.start()

    for process in processes:
        process.join()

    print("Without Lock Final balance:", account.balance.value)

    print("----------------After Lock--------------------")
    accountLock = BankAccountWithLock(balance=1000)

    # List to keep track of all the processes
    processesLock = []

    # Create a lock to synchronize access to the shared resource (balance)
    lock = multiprocessing.Lock()

    # Create two processes that will perform the deposit operation concurrently
    process1 = multiprocessing.Process(target=accountLock.deposit, args=(100, lock))
    process2 = multiprocessing.Process(target=accountLock.deposit, args=(100, lock))

    # Add the processes to the list
    processesLock.append(process1)
    processesLock.append(process2)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for all processes to finish
    for process in processesLock:
        process.join()

    print("With Lock Final balance:",
          accountLock.balance.value)  # Print the final balance after all processes have completed
