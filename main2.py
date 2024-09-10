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