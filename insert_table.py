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
cur.execute("INSERT INTO todo (ID,NAME,EMAIL) VALUES(1, 'Sanjarbek', 'sanj@rbek.com')")
conn.commit()
print("Data inserted sucsesfuly")
conn.close()
print("created table sucsesfuly")