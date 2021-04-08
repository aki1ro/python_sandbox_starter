from mysql import connector #used to pass sql commands to database
from datetime import datetime #used to give the date and time

db = connector.connect(
   host="localhost",
   user="root",
   passwd="root",
   database="testdatabase"
   )

mycursor = db.cursor()


# mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O'), id int PRIMARY KEY NOT NULL AUTO_INCREMENT)") <--- used to create a table named "Test" this name has the NOT NULL attribute meaning no NULL values, created meaning created at this time, and datetime references our datetime module for that information. ENUM is used to allow to select between a few different values given and will be accepted for the given block, in this case being 'gender' 

# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("NICK", datetime.now(), "M"))

# mycursor.execute("CREATE DATABASE testdatabase") <--- used to create database

# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)") #This code uses the execute function to run the aql command CREATE TABLE to create a table called 'Person', this table will have a column called 'name' that will be a variable character length up to 50, the 'age' column will have a smallint (integer that takes up a small amount of memory space -32000 - 3200 is what this covers) and the personID is an int which is the PRIMARY KEY (which is a unique value associated with each column in a table). This is set to AUTO_INCREMENT to increment automatically and be different so it can be called uniquely. 

# mycursor.execute("DESCRIBE Person") <--- used to look at the table we created "Describes the Person table"

# mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", ("Rick", 22)) #<--- %s used to pass a string value. This code is used to insert values into a table.
# db.commit() #used to commit changes to the database
# mycursor.execute("SELECT * FROM Person") #<--- used to select all values from table person

# mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC") #<--- used to select all values from the table Test 'where' is used to specify a condition, in this case the condition being gender is equal to M. ORDER BY is used to order the selection in this case by id and DESC is descending so higher to lower value


for x in mycursor:
   print(x)

