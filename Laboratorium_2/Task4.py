import multiprocessing

def calculate_power_sum(start, end):
    result = {}
    for num in range(start, end + 1):
        result[num] = sum([num**i for i in range(1, 101)])
    return result

def main():
    start_range = 1
    end_range = 1000
    num_processes = 4

    pool = multiprocessing.Pool(num_processes)
    chunk_size = (end_range - start_range) // num_processes
    ranges = [(i, min(i + chunk_size, end_range)) for i in range(start_range, end_range, chunk_size)]

    results = pool.starmap(calculate_power_sum, ranges)
    pool.close()
    pool.join()

    combined_result = {}
    for result in results:
        combined_result.update(result)

    return combined_result

if __name__ == "__main__":
    power_sums = main()
    print("Sumy kolejnych stu potęg dla każdej liczby w zakresie:", power_sums)
