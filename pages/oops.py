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
cursor.execute("select * from students")
data = cursor.fetchall()
conn.close()



class button_show:
    def __init__(self,button_name,user_name):
        st.button(button_name)
        st.write(user_name)
        st.divider()

for i in data:
    button_show(f"{i[0]}",f"{i[1]}")

