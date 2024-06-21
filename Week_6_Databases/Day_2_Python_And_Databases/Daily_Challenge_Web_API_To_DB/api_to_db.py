import random
import requests
import psycopg2

HOST = "localhost"
PORT = "5432"
DATABASE = "TTA_14"
USERNAME = "postgres"
PASSWORD = "130891lion"
TABLE = "countries"

API_URL = "https://restcountries.com/v2/all?fields=name,capital,flag,subregion,population"


def get_random_countries():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching countries: {response.status_code}")


def save_countries(countries):
    conn = psycopg2.connect(host=HOST, port=PORT, user=USERNAME,
                            password=PASSWORD, database=DATABASE)
    cur = conn.cursor()

    for country in random.sample(countries, 10):
        try:
            name = country["name"]
            if "capital" in country:
                capital = country["capital"]
            else:
                capital = "N/A"
            flag = country["flag"]
            subregion = country["subregion"]
            population = country["population"]

            insert_query = """
      INSERT INTO countries (name,capital,flag,subregion,population) VALUES (%s,%s,%s,%s,%s)
      """
            cur.execute(insert_query, (name, capital,
                        flag, subregion, population))
            conn.commit()

        except Exception as e:
            print(f"Error saving country {name}: {e}")
            conn.rollback()
    cur.close()
    conn.close()


contries = get_random_countries()
save_countries(contries)
