import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="plugin_member"
)

cursor = db.cursor()
sql = "SELECT * FROM member"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)
