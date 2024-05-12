import threading
import queue
import logging 

logging.basicConfig(level = logging.INFO)
class Producer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(1, 101):  
            self.queue.put(i)

class Consumer(threading.Thread):
    def __init__(self, queue, name, predicate):
        super().__init__()
        self.queue = queue
        self.name = name
        self.predicate = predicate

    def run(self):
        while True:
            item = self.queue.get()
            if item is None:
                break
            if self.predicate(item):
                logging.info(f"{self.name} consumed: {item}")
            self.queue.task_done()

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def main():
    q = queue.Queue()
    producer = Producer(q)
    consumer_even = Consumer(q, "Consumer Even", is_even)
    consumer_odd = Consumer(q, "Consumer Odd", is_odd)

    producer.start()
    consumer_even.start()
    consumer_odd.start()

    producer.join()
    q.join()  
    q.put(None)
    q.put(None)

    consumer_even.join()
    consumer_odd.join()

if __name__ == "__main__":
    main()
