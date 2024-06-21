import psycopg2

HOST = "localhost"
PORT = "5432"
DATABASE = "Restaurant"
USERNAME = "postgres"
PASSWORD = "130891lion"
TABLE = "Menu_Items"

conn = psycopg2.connect(host=HOST, port=PORT, user=USERNAME,
                        password=PASSWORD, database=DATABASE)


class MenuItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        cur = conn.cursor()
        data = (self.name, self.price)
        query = f"INSERT INTO {
            TABLE} (item_name, item_price) VALUES (%s, %s) ON CONFLICT (item_name) DO NOTHING"
        cur.execute(query, data)
        conn.commit()
        cur.close()

    def delete(self):
        cur = conn.cursor()
        data = (self.name, self.price)
        query = f"DELETE FROM {TABLE} WHERE item_name=%s and item_price=%s"
        cur.execute(query, data)
        conn.commit()
        cur.close()

    def update(self, new_name, new_price):
        cur = conn.cursor()
        try:
            data = (self.name, self.price)
            query = f"UPDATE {TABLE} SET item_name='{new_name}',item_price={
                new_price} WHERE item_name=%s and item_price=%s"
            cur.execute(query, data)
            conn.commit()
            cur.close()
        except psycopg2.errors.UniqueViolation as e:
            print(f"Error: Item with name '{new_name}' already exists!")
            conn.rollback()
        finally:
            if conn:
                cur.close()
