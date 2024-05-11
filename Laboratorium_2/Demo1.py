import requests
from bs4 import BeautifulSoup
import time
import logging 


logging.basicConfig(level = logging.INFO)
titles  = []


def download_site(url, session):
    global titles
     
    with session.get(url) as response:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        event_titles = soup.find_all('h3', class_='tribe-events-calendar-list__event-title')

        for title_raw in event_titles:
            title = title_raw.text.strip() 
            logging.info(f"Pobrano tytul: {title}")
            titles.append(title)
        


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [f"https://wsei.edu.pl/wydarzenia/lista/strona/{i}/?eventDisplay=past" for i in range(1,11)]
    start = time.time()
    download_all_sites(sites)
    logging.info(f"Pobrano {len(titles)} tytulow in {time.time() - start} seconds")
    