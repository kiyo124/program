import psycopg2

conn=psycopg2.connect(dbname='postgres', user='postgres',password='siaas', host='localhost', port='5433')
cur=conn.cursor()

def table():
    
    cur.execute('''create table if not exists students(roll_no int, name text, age int);''')
    print("Table created Sucessfully")


table()

def insert():
    a=input("Do you want to insert data? (yes/no): ")
    
    if a.lower()=='yes':
        
        roll_no=int(input("Enter Roll No: "))
        name=input('Enter Name: ')
        age=int(input('Enter Age: '))
        query= '''insert into students(roll_no, name, age) values(%s, %s, %s);'''
        cur.execute(query, (roll_no, name, age))
        print("Data Inserted Sucessfully")
    
    else:
        
        print("Data not inserted")

insert()

def extract():
    rollno=input("enter a roll number to extract data")
    query='''select * from students where roll_no=(%s);'''
    cur.execute(query , (rollno))
    
    print(cur.fetchone())

extract()

conn.commit()
conn.close()



