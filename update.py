import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="plugin_member"
)

cursor = db.cursor()
sql = "UPDATE member SET name=%s, address=%s WHERE member_id=%s"
val = ("setiyawan", "wonogiri", 1)
cursor.execute(sql, val)

db.commit()

print("{} data diubah".format(cursor.rowcount))