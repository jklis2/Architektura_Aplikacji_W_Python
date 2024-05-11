import threading
import queue
import time

def producer(queue, max_numbers):
    for number in range(max_numbers):
        queue.put(number)
        print(f'Produced: {number}')
        time.sleep(0.1)
    queue.put(None)

def consumer_even(queue, name):
    while True:
        number = queue.get()
        if number is None:
            queue.put(None)
            break
        if number % 2 == 0:
            print(f'{name} consumed (even): {number}')

def consumer_odd(queue, name):
    while True:
        number = queue.get()
        if number is None:
            queue.put(None)
            break
        if number % 2 != 0:
            print(f'{name} consumed (odd): {number}')

if __name__ == '__main__':
    q = queue.Queue()
    max_numbers = 20

    producer_thread = threading.Thread(target=producer, args=(q, max_numbers))
    
    consumer_even_thread = threading.Thread(target=consumer_even, args=(q, 'Consumer 1'))
    consumer_odd_thread = threading.Thread(target=consumer_odd, args=(q, 'Consumer 2'))

    producer_thread.start()
    consumer_even_thread.start()
    consumer_odd_thread.start()

    producer_thread.join()
    consumer_even_thread.join()
    consumer_odd_thread.join()

    print("All threads have finished execution.")
