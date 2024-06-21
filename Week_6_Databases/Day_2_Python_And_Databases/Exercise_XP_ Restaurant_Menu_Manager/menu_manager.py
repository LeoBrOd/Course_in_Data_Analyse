import psycopg2
from menu_item import MenuItem

HOST = "localhost"
PORT = "5432"
DATABASE = "Restaurant"
USERNAME = "postgres"
PASSWORD = "130891lion"
TABLE = "Menu_Items"

conn = psycopg2.connect(host=HOST, port=PORT, user=USERNAME,
                        password=PASSWORD, database=DATABASE)


class MenuManager ():
    @classmethod
    def get_by_name(cls, name):
        cur = conn.cursor()
        query = f"SELECT * FROM {TABLE} WHERE item_name ='{name}'"
        cur.execute(query)
        item_data = cur.fetchone()
        cur.close()
        if item_data:
            return MenuItem(item_data[1], item_data[2])
        else:
            return None

    @classmethod
    def all_items(cls):
        cur = conn.cursor()
        cur.execute(f"SELECT item_name, item_price FROM {TABLE}")
        items_data = cur.fetchall()
        cur.close()
        return items_data


if __name__ == "__main__":
    item = MenuItem('Burger', 35)
    item.save()
    # item.delete()
    item = MenuItem('Burger', 35)
    item.save()
    item.update('Veggie Burger', 37)
    item2 = MenuManager.get_by_name('Beef Stew')
    items = MenuManager.all_items()
    print(items)