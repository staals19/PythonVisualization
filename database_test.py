#downloaded MySQL and connected to the database through mySQL command line
import MySQLdb

#connecting to database using relevant info (host, port, user, password, database name), all of which should be shown during mySQL connection
db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='',db='world')

#setting up a cursor
cur = db.cursor()

#implementing SQL
cur.execute('SELECT * FROM country')

#implementing python code
#ex: printing the first row in each
for row in cur.fetchall():
	print row[0]
	
db.close()