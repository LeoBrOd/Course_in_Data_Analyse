import requests
import time


def measure_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        response.raise_for_status()
        end_time = time.time()
        loading_time = end_time - start_time
        return loading_time

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


websites = [
    "https://www.google.com",
    "https://www.ynet.co.il",
    "https://www.imdb.com"
]

for i in websites:
    load_time = measure_load_time(i)
    if load_time:
        print(f"For {i} it takes {load_time:} seconds to load")
