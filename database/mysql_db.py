import mysql.connector

db = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="testdatabase",
)

cursor = db.cursor()

