import os
import psycopg2

# Batchen123@

conn = psycopg2.connect("postgresql://postgres:[Batchen123@]@db.fyyplymnrghrjjtlbziy.supabase.co:5432/postgres")
cur = conn.cursor()

cur.execute("SELECT * FROM wagons")
rows = cur.fetchall()
print(rows)

cur.close()
conn.close()

