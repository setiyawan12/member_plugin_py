import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="plugin_member"
)

cursor = db.cursor()
sql = "INSERT INTO member (name, address) VALUES (%s, %s)"
val = ("setiyawan", "Tegal")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))
