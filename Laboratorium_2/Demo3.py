import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    start_range = 1
    end_range = 1000000
    num_processes = 4

    pool = multiprocessing.Pool(num_processes)
    chunk_size = (end_range - start_range) // num_processes
    ranges = [(i, min(i + chunk_size, end_range)) for i in range(start_range, end_range, chunk_size)]

    results = pool.starmap(find_primes, ranges)
    pool.close()
    pool.join()

    prime_numbers = []
    for result in results:
        prime_numbers.extend(result)

    return prime_numbers

if __name__ == "__main__":
    prime_numbers = main()
    print("Prime numbers found:", prime_numbers)
    
    
    