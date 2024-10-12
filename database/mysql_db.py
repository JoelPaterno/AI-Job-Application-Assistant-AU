import mysql.connector

db = mysql.connector.connect(
    user="root",
    password="joel1234",
    host="192.168.0.105",
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS testdatabase")