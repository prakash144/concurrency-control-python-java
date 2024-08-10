# We use code profilers to professionally and systematically analyze code to figure out what is causing slow-downs
# and where. This can dramatically help optimize slow code and save a lot of time reading through code. Probably the
# most useful tool for a Python Programmer.
# Video link - https://www.youtube.com/watch?v=i24jvJ-PN84&list=PLijwb6y4zksTdgk7A2De1cHrwgNbuzNdT&index=7

# For viewing the stats we will utilise SnakeViz i.e. SnakeViz is a browser based graphical viewer for the output of
# Python’s cProfile module and an alternative to using the standard library pstats module. link -
# https://jiffyclub.github.io/snakeviz/

import random
import time
import cProfile
import pstats


# Simulate fetching customer orders from a database
def fetch_orders():
    orders = []
    for _ in range(1000000):
        order = {
            "order_id": random.randint(1, 1000000),
            "customer_id": random.randint(1, 100),
            "items": [f"item_{i}" for i in range(random.randint(1, 5))],
        }
        orders.append(order)
    return orders


# Simulate processing orders and calculating total price
def process_orders(orders):
    total_revenue = 0
    for order in orders:
        order_total = sum(random.uniform(10, 100) for _ in order["items"])
        total_revenue += order_total
    return total_revenue


# Simulate generating a report for the finance department
def generate_report(revenue):
    time.sleep(2)
    report = f"Total Revenue: {revenue:.2f}"
    return report


# Main function to simulate the order processing workflow
def main():
    order = fetch_orders()
    revenue = process_orders(order)
    report = generate_report(revenue)
    print(report)


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats("cumtime")
    stats.print_stats()
    stats.dump_stats("profiling_results.prof")
