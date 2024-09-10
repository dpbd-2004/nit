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
    
conn = create_connection()
cursor = conn.cursor()
cursor.execute("select count(distinct age and grade) from students;")
data = cursor.fetchall()
conn.commit()
conn.close()

st.write(data)