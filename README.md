# Concurrency Control in Distributed Systems

In the context of system design, especially for a Google Software Development Engineer (SDE) role, understanding concurrency control is crucial for designing scalable, reliable, and efficient systems.
But first, I briefly explain threads, processes and the differences between parallelism and concurrency. 

---

## Multithreading

- **Definition**: Running multiple threads concurrently within a single process.

- **System Design Perspective**:
  - Useful for tasks that can be parallelized, such as handling multiple client requests in a web server.

- **Real-life Example**: 
  - **Web Browsers** use multiple threads to load different tabs and UI components simultaneously.

- **Trade-offs**:
  - **Pros**: Efficient CPU utilization, improved responsiveness.
  - **Cons**: Complexity in managing thread synchronization and potential race conditions.

---

## Multiprocessing

- **Definition**: Running multiple processes simultaneously, each with its own memory space.

- **System Design Perspective**:
  - Suitable for CPU-bound operations where processes can run in isolation.

- **Real-life Example**:
  - **Database Servers** often use multiprocessing to handle different database queries in separate processes, providing isolation and fault tolerance.

- **Trade-offs**:
  - **Pros**: Better fault isolation, can take advantage of multiple CPU cores.
  - **Cons**: Higher memory consumption compared to multithreading, more complex inter-process communication (IPC).

---

## Thread

- **Definition**: The smallest unit of execution within a process.

- **System Design Perspective**:
  - Threads allow a program to perform multiple operations simultaneously.

- **Real-life Example**: 
  - **Chat Applications** use threads to handle incoming and outgoing messages, notifications, and other background tasks.

- **Trade-offs**:
  - **Pros**: Lightweight, lower context switching overhead than processes.
  - **Cons**: Risk of shared data corruption, complex synchronization required.

---

## Concurrency Control in Distributed Systems

- **Definition**: Mechanisms to manage simultaneous operations without conflicts in a distributed environment.

- **System Design Perspective**:
  - Critical for ensuring data consistency and integrity across distributed components.

- **Real-life Example**: 
  - **Distributed Databases** like **Google Spanner** use concurrency control to manage transactions across multiple data centers.

### Key Techniques and Trade-offs:

#### Locks
- **Definition**: Prevent multiple transactions from accessing the same data simultaneously.
  - **Advantages**: Ensures data consistency.
  - **Disadvantages**: Can lead to **deadlocks** and reduce system throughput.

#### Optimistic vs. Pessimistic Locking
- **Optimistic Locking**: Assumes minimal conflict and checks for data consistency at the end of a transaction.
  - **Advantages**: High throughput in low-contention scenarios.
  - **Disadvantages**: Can result in frequent rollbacks in high-contention scenarios.
- **Pessimistic Locking**: Locks resources early to avoid conflicts.
  - **Advantages**: Prevents data conflicts.
  - **Disadvantages**: Can cause **resource contention** and reduce concurrency.

#### Semaphores
- **Definition**: Control access to a finite number of resources.
  - **Advantages**: Simple to implement and understand.
  - **Disadvantages**: Potential for **deadlocks** if not managed carefully.

#### Transactions (ACID Properties)
- **Definition**: Ensure a series of operations are atomic, consistent, isolated, and durable.
  - **Advantages**: Guarantees data consistency and integrity.
  - **Disadvantages**: Can be resource-intensive and complex to implement in a distributed system.

#### Distributed Consensus Algorithms
- **Definition**: Such as **Paxos** or **Raft**, for achieving agreement on shared state in distributed systems.
  - **Advantages**: Ensure all nodes agree on the same state, critical for consistency.
  - **Disadvantages**: Can be slow and complex, especially in large systems.

#### Leader Election
- **Definition**: Mechanisms for electing a leader in distributed systems to coordinate actions.
  - **Advantages**: Simplifies decision-making and conflict resolution.
  - **Disadvantages**: **Single point of failure** if not handled properly.

---

## Parallelism vs. Concurrency

## Concurrency
- Involves multiple tasks making progress within overlapping time frames.
- Tasks may start, run, and complete in overlapping time periods but are not necessarily executed simultaneously.
- Focuses on managing access to shared resources.
- Typically achieved through task switching on a single core.

## Parallelism
- Involves executing multiple tasks simultaneously.
- Tasks are executed at the same time on multiple cores or processors.
- Focuses on increasing computational speed by dividing tasks into smaller sub-tasks.
- Requires multiple processing units (e.g., multi-core processors).

#### Key Points:
- **Concurrency** focuses on task structure, while parallelism focuses on task execution.
- **Concurrency** can lead to parallelism if multiple cores are available.
- **Parallelism** without concurrency is possible in data-parallel operations where no task switching is needed.

---

### Multithreading and Multiprocessing


**Python:** Due to the Global Interpreter Lock (GIL) in Python, multithreading only achieves concurrency, not parallelism.
- **Multithreading:** The Global Interpreter Lock (GIL) prevents multiple threads from executing Python bytecode in parallel within a single process, so Python threads achieve concurrency (interleaving tasks) but not parallelism (true simultaneous execution on multiple cores).
- **Multiprocessing:** By using separate processes instead of threads, Python can bypass the GIL. Each process has its own Python interpreter and memory space, allowing for true parallelism on multi-core processors.
- **Note:** In contrast, Java does not have the GIL and can achieve both concurrency and parallelism through multithreading.

  - **I/O-bound Tasks**: Python's multithreading is effective for I/O-bound tasks, such as reading from files or waiting for network responses. The Global Interpreter Lock (GIL) is released during I/O operations, allowing other threads to execute concurrently.
  - **CPU-bound Tasks**: For CPU-bound tasks, where the program spends most of its time performing calculations, Python's multithreading does not provide performance benefits due to the GIL. In these cases, using the `multiprocessing` module is recommended, as it creates separate processes that can run on different CPU cores in parallel.



**Java:** Unlike Python, Java does not have a Global Interpreter Lock (GIL), so multiple threads can run in parallel on multi-core systems, fully utilizing the CPU's power.
- In Java, multithreading can achieve both concurrency and parallelism.
- **Concurrency:** Java threads can run concurrently, meaning they can manage multiple tasks at once by switching between them.
- **Parallelism:** Java can achieve true parallelism if it runs threads on multiple CPU cores, allowing different tasks to execute simultaneously.

---

### Resources:
- [ Threading in Python ](https://youtu.be/WWdtGdNzQoo?list=PLijwb6y4zksTdgk7A2De1cHrwgNbuzNdT)
- [ Achieve TRUE Parallelism in Python with Multiprocessing ](https://www.youtube.com/watch?v=kd7LcUjFNJo&list=PLijwb6y4zksTdgk7A2De1cHrwgNbuzNdT&index=4)

