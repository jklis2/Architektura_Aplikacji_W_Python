import asyncio
import nest_asyncio
import logging 

nest_asyncio.apply()
logging.basicConfig(level = logging.INFO)

async def produce_data(buffer):
    for i in range(1, 11):  
        await asyncio.sleep(1)  
        buffer.append(i)
        logging.info(f"Produced: {i}")

async def consume_data(buffer):
    while True:
        await asyncio.sleep(0.5) 
        if buffer:
            data = buffer.pop(0)
            logging.info(f"Consumed: {data}")

async def main():
    buffer = []
    producer_task = asyncio.create_task(produce_data(buffer))
    consumer_task = asyncio.create_task(consume_data(buffer))
    await asyncio.gather(producer_task, consumer_task)

asyncio.run(main())
