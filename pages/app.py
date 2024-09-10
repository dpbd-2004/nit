import streamlit as st
import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        conn = sqlite3.connect('django_app.db')
        return conn
    except Error as e:
        st.error(f"Error: '{e}'")
        return None

conn = create_connection()
cursor = conn.cursor()
cursor.execute(f"select count(distinct grade) from students;")
data = cursor.fetchall()
conn.commit()
conn.close()

st.write(data)
