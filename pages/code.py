import streamlit as st

st.title("http://10.10.37.59:8501/")

st.code("""
-- creating a database
create database django_app;

-- selecting the django_app 
use django_app;

-- Creating a table for the application 
create table students(
id int primary key auto_increment,
name varchar(50),
age int,
grade char(1)
);

-- view everything from the table
select * from students;

-- insert a data to the table
insert into students(name, age, grade) values ('kiran', 29, 'F');

-- view specific content from the table
select age as student_age, name as student_name from students;

-- view only unique content
select distinct name from students;

-- updating the content based on id
update students set name='Gowtham' where id=1;

-- updating the content based on name - you will get error like Disable safe mode
update students set name='Dharani' where name='dharani';

-- Disabling the safe mode
set sql_safe_updates=0;

-- updating the content based on name - it will change all the names
update students set name='Dharani' where name='dharani';

-- delete a item from the table
delete from students where name="Dharani" and age=20;

-- Done with the basics things. Now start with Aggregate
select count(*) from students;

-- count the total unique values in grade
select count(distinct grade) from students;
select count(distinct age) from students;
select count(distinct age and grade) from students;

-- finding sum of the age
select sum(age) from students;

-- finding sum of the grade - it will return nothing
select sum(grade) from students;

-- finding average in the age (102/5) = 20.4000;
select avg(age) from students;
""")

st.title("app.py code")
st.code("""
import streamlit as st
import sqlite3
from sqlite3 import Error

# Function to create a SQLite connection
def create_connection():
    try:
        conn = sqlite3.connect('django_app.db')
        return conn
    except Error as e:
        st.error(f"Error: '{e}'")
        return None
    
conn = create_connection()
cursor = conn.cursor()
cursor.execute("select count(distinct age and grade) from students;")
data = cursor.fetchall()
conn.commit()
conn.close()

st.write(data)
""")