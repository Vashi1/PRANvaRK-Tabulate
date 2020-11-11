# To create the users for the database
import mysql.connector as sql
myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@")
cur = myql.cursor()
cur.execute("create user 'Rakshith'@localhost identified by 'Rakshith1@'")
myql.commit()
cur.execute("grant all privileges on *.* to user 'Rakshith'@localhost identified by 'Rakshith1@'")
myql.commit()
cur.execute("flush privileges")
myql.commit()