import multiprocessing
from math import isqrt
from itertools import compress

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_twin_primes(start, end):
    """Find twin primes in the given range."""
    primes = [i for i in range(start, end + 1) if is_prime(i)]
    twin_primes = [(primes[i], primes[i + 1]) for i in range(len(primes) - 1) if primes[i + 1] - primes[i] == 2]
    return twin_primes

def worker(start, end, queue):
    """Worker function for multiprocessing."""
    result = find_twin_primes(start, end)
    queue.put(result)

def main():
    RANGE_START = 1
    RANGE_END = 100000  
    NUM_PROCESSES = 4
    
    chunk_size = (RANGE_END - RANGE_START) // NUM_PROCESSES
    
    queue = multiprocessing.Queue()
    
    processes = []
    for i in range(NUM_PROCESSES):
        start = RANGE_START + i * chunk_size
        end = start + chunk_size - 1
        if i == NUM_PROCESSES - 1: 
            end = RANGE_END
        p = multiprocessing.Process(target=worker, args=(start, end, queue))
        processes.append(p)
        p.start()
    
    twin_primes = []
    for _ in range(NUM_PROCESSES):
        twin_primes.extend(queue.get())
    
    for p in processes:
        p.join()
    
    for pair in twin_primes:
        print(pair)

if __name__ == "__main__":
    main()
