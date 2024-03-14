"""Parallelism Examples"""
# Multiprocessing

import multiprocessing
import time

def square_numbers(numbers, result_queue):
    for num in numbers:
        result_queue.put(num * num)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result_queue = multiprocessing.Queue()

    # Create a process pool
    processes = []
    for _ in range(2):  # Using 2 processes for demonstration
        process = multiprocessing.Process(target=square_numbers, args=(numbers, result_queue))
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Collect results from the queue
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    print("Results:", results)

#Parallel Computing with Dask
# import dask.array as da
# import numpy as np

# # Create a large random array
# arr = da.random.random((10000, 10000), chunks=(1000, 1000))

# # Perform a parallel computation (e.g., matrix multiplication)
# result = arr.dot(arr.T).mean(axis=0)

# print(result.compute())
