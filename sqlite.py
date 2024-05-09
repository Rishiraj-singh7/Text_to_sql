import sqlite3

## Connect to SQLite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record, create table 

cursor=connection.cursor()

## Create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25));

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Rahul','Data  Science','A')''')
cursor.execute('''Insert Into STUDENT values('Sudhir','Data  Science','B')''')
cursor.execute('''Insert Into STUDENT values('Danush','Data  Engineer','A')''')
cursor.execute('''Insert Into STUDENT values('Vikas','DEVOPS','A')''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A')''')

## Display all the records 

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)