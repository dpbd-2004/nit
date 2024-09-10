import streamlit as st
import sqlite3
from sqlite3 import Error

with st.sidebar:
    st.subheader("10.10.37.59:8501")

# Function to create a SQLite connection
def create_connection():
    try:
        conn = sqlite3.connect('django_app.db')
        return conn
    except Error as e:
        st.error(f"Error: '{e}'")
        return None

# Function to create the students table if it doesn't exist
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade TEXT NOT NULL
            )
        ''')
        conn.commit()
    except Error as e:
        st.error(f"Error: '{e}'")

# Function to insert user data into SQLite
def insert_data(conn, name, age, result):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)"
        values = (name, age, result)
        cursor.execute(query, values)
        conn.commit()
        st.success("Data added successfully")
    except Error as e:
        st.error(f"Error: '{e}'")

# Streamlit app code
RESULT_OPTIONS = ["P", "F", "A"]

st.title("Hello There")
name = st.text_input("Enter Your Name")
age = st.number_input("Enter your age", help="Enter your age in this box")
result = st.selectbox("Result", options=RESULT_OPTIONS)

# On button click, insert data into SQLite
if st.button("Add"):
    if name and age:
        conn = create_connection()
        if conn:
            create_table(conn)
            insert_data(conn, name, int(age), result)
            conn.close()
    else:
        st.warning("Please fill in all the details")


conn = create_connection()
cursor = conn.cursor()
cursor.execute("select * from students")
data = cursor.fetchall()
conn.close()
st.data_editor(data)

st.title("Update")
id_select = st.number_input("Enter the ID")
name_change = st.text_input("Enter the name")

if st.button("Update"):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(f"update students set name='{name_change}' where id={id_select};")
        conn.commit()
        conn.close()
        st.rerun()
    except Error as e:
        st.error(f"Error: '{e}'")

st.title("Delete")
delete_id = st.number_input("Enter the id to delete")
if st.button("Delete"):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(f"delete from students where id={delete_id};")
        conn.commit()
        conn.close()
        st.rerun()
    except Error as e:
        st.error(f"Error: '{e}'")