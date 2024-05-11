import threading
import time
import requests

def download_site(url, session):
    with session.get(url) as response:
        print(response.content)

def download_all_sites(sites):
    with requests.Session() as session:
        threads = []
        for url in sites:
            thread = threading.Thread(target=lambda: download_site(url, session))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

sites = [f"https://catfact.ninja/fact" for i in range (1, 101)]
startTime = time.time()
download_all_sites(sites)
endTime = time.time()
print(f"Total time: {endTime - startTime}")