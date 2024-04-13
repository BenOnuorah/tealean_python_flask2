import mysql.connector
from mysql.connector import Error

def connect_db():
		#create and connect to the database
		db = mysql.connector.connect(
			host="127.0.0.1",
			database='tea_flask',
			user="root",
			password="onuorah12"
			)
		conn = db.cursor(buffered=True)
		return conn	