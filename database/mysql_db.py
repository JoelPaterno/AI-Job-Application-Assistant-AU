import mysql.connector

db = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="testdatabase",
)

cursor = db.cursor()

#cursor.execute("DROP TABLE IF EXISTS JobPost")

#cursor.execute("CREATE TABLE JobPost (postID INT AUTO_INCREMENT PRIMARY KEY, site VARCHAR(255), title VARCHAR(255), company VARCHAR(255), location VARCHAR(255), jobType VARCHAR(255), description TEXT(20000), job_url VARCHAR(255), job_url_direct VARCHAR(255), date_posted VARCHAR(255))")

#cursor.execute("SELECT * FROM JobPost")