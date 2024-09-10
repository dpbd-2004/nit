# MySQL DB should be installed
# You should have a DB with name django_app
# You should have a table name with students with name, age and grade as a column name

import streamlit as st
import mysql.connector
from mysql.connector import Error

# Function to create a MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",            # Replace with your MySQL username
            passwd="root",  # Replace with your MySQL password
            database="django_app" # Replace with your database name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error: '{e}'")
        return None

# Function to insert user data into MySQL
def insert_data(connection, name, age, result):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
        values = (name, age, result)
        cursor.execute(query, values)
        connection.commit()
        st.success("Data added successfully")
    except Error as e:
        st.error(f"Error: '{e}'")

# Streamlit app code
RESULT_OPTIONS = ["P", "F", "A"]

st.title("Hello There")
name = st.text_input("Enter Your Name")
age = st.number_input("Enter your age", help="Enter your age in this box")
result = st.selectbox("Result", options=RESULT_OPTIONS)

# On button click, insert data into MySQL
if st.button("Add"):
    if name and age:
        connection = create_connection()
        if connection:
            insert_data(connection, name, int(age), result)
            connection.close()
    else:
        st.warning("Please fill in all the details")
