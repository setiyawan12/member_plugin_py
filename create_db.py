import mysql.connector

db = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE plugin_member")

print("Database berasil di buat")