import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="plugin_member"
)

cursor = db.cursor()
sql = "DELETE FROM member WHERE member_id=%s"
val = (1, )
cursor.execute(sql, val)

db.commit()

print("{} data dihapus".format(cursor.rowcount))