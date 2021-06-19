import psycopg2

DB_NAME="postgres"
DB_USER="postgres"
DB_PASS="Sanjar0302$$"
DB_HOST="localhost"
DB_PORT="5432"

conn = psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASS,
                                  host=DB_HOST,port=DB_PORT)

print("Databases connect sucsesfuly")

cur = conn.cursor()
cur.execute("""
CREATE TABLE todo
(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
EMAIL TEXT NOT NULL
)
""")
conn.commit()
print("created table sucsesfuly")