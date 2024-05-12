import time
import aiohttp
import asyncio
import nest_asyncio
import logging 

nest_asyncio.apply()
logging.basicConfig(level = logging.INFO)

RANDOM_USER_URL = 'https://randomuser.me/api/'

async def fetch_user_data(session):
    async with session.get(RANDOM_USER_URL) as response:
        return await response.json(content_type=None)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_user_data(session) for _ in range(10)]
        return await asyncio.gather(*tasks) 

if __name__ == "__main__":
    start = time.time()
    users = asyncio.run(main())
    emails = [user['results'][0]['email'] for user in users if user is not None]

    logging.info(f"Pobrano {len(emails)} maili w {time.time() - start} sekund")
    logging.info(f"maile: {emails}")
    
    
    
    
    