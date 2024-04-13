import sqlite3 
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def connect_db():
		#create and connect to the database
		conn = sqlite3.connect(dir_path+'/tealearn_grades.db', check_same_thread=False) 
		return conn