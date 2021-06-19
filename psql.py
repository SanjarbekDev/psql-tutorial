import psycopg2

DB_NAME="nnzrzddd"
DB_USER="nnzrzddd"
DB_PASS="EUk6gDdcaEPfr1h4wUxQImCtzJG4cjxZ"
DB_HOST="batyr.db.elephantsql.com"
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