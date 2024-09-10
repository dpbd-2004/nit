import streamlit as st
import sqlite3
from sqlite3 import Error

<<<<<<< HEAD
=======
# Function to create a SQLite connection
>>>>>>> 27fdc69cc5dd40c1f6f1ca0a5477ba8d1f443cb0
def create_connection():
    try:
        conn = sqlite3.connect('django_app.db')
        return conn
    except Error as e:
        st.error(f"Error: '{e}'")
        return None
<<<<<<< HEAD

=======
    
>>>>>>> 27fdc69cc5dd40c1f6f1ca0a5477ba8d1f443cb0
conn = create_connection()
cursor = conn.cursor()
cursor.execute("select * from students")
data = cursor.fetchall()
conn.close()

<<<<<<< HEAD


class button_show:
    def __init__(self,button_name,user_name):
=======
# for i in data:
#     st.write(i)
    
class button_show:
    def __init__(self, button_name, user_name):
>>>>>>> 27fdc69cc5dd40c1f6f1ca0a5477ba8d1f443cb0
        st.button(button_name)
        st.write(user_name)
        st.divider()

for i in data:
<<<<<<< HEAD
    button_show(f"{i[0]}",f"{i[1]}")
=======
    button_show(f"{i[0]}", i[1])
>>>>>>> 27fdc69cc5dd40c1f6f1ca0a5477ba8d1f443cb0

