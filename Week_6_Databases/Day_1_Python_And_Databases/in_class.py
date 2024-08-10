from faker import Faker
from fake2db import Fake2Db
import psycopg2

con=psycopg2.connect(database='postgres',user='postgres', password='130891lion', host='localhost', port='5432')
con.autocommit=True
cur=con.cursor()
new_db="test_db"
cur.execute(f"CREATE database {new_db}")
cur.close()
con.close()

generator=Fake2Db(database='postgresql',host="localhost",port='5432',username='postgres',password='130891lion',database="new_db")
database_path="new_db"
generator.custom(data_type="user",rows=200,custom="name email city")
