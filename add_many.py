import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="plugin_member"
)

cursor = db.cursor()
sql = "INSERT INTO member (name, address) VALUES (%s, %s)"
values = [
  ("fadzlan", "Jakarta"),
  ("ade", "Surabaya"),
  ("faqih", "Bandung"),
  ("chotimah", "Depok")
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data ditambahkan".format(len(values)))