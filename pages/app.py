import streamlit as st
import sqlite3
from sqlite3 import Error

<<<<<<< HEAD
=======
with st.sidebar:
    st.subheader("10.10.37.59:8501")

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

conn = create_connection()
cursor = conn.cursor()
cursor.execute(f"select count(distinct grade) from students;")
=======
    
conn = create_connection()
cursor = conn.cursor()
cursor.execute("select count(distinct age and grade) from students;")
>>>>>>> 27fdc69cc5dd40c1f6f1ca0a5477ba8d1f443cb0
data = cursor.fetchall()
conn.commit()
conn.close()

<<<<<<< HEAD
st.write(data)
=======
st.write(data)
>>>>>>> 27fdc69cc5dd40c1f6f1ca0a5477ba8d1f443cb0
