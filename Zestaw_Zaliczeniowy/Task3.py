import requests
import threading

def fetch_universities(country, result):
    try:
        response = requests.get(f"http://universities.hipolabs.com/search?country={country}")
        data = response.json()
        university_names = [university['name'] for university in data]
        result[country] = university_names
    except Exception as e:
        result[country] = f"Error: {str(e)}"

def main():
    countries = ["United States", "Canada", "United Kingdom", "Australia", "Germany", "France", "Italy", "Spain", "Japan", "China", "India", "Brazil", "South Korea", "Russia", "Mexico"]
    threads = []
    result = {}

    for country in countries:
        thread = threading.Thread(target=fetch_universities, args=(country, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for country, universities in result.items():
        print(f"{country}: {universities}")

if __name__ == "__main__":
    main()
