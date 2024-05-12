"""
import time
import requests

CAT_API_URL = 'https://catfact.ninja/fact'

cat_facts = []
start = time.time()
for _ in range(10):
    cat_facts.append(requests.get(CAT_API_URL).json().get('fact'))

print(f"Pobrano fakty w {time.time() - start} sekund")
print(cat_facts)
"""

import time
import requests
from concurrent.futures import ThreadPoolExecutor

CAT_API_URL = 'https://catfact.ninja/fact'

cat_facts = []
def fetch_cat_fact(n):
    return requests.get(CAT_API_URL).json().get('fact')
    
if __name__ == "__main__":
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        cat_facts = executor.map(fetch_cat_fact, range(10))

    print(f"Pobrano fakty w {time.time() - start} sekund")
    print(list(cat_facts))