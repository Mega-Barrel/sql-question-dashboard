""" streamlit_app.py"""

import streamlit as st
import psycopg2

st.set_page_config(
    page_title="SQL Question Tracker",
    page_icon='🎯',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://github.com/Mega-Barrel/sql-question-dashboard/issues",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Set title
st.title('Daily SQL Question Tracker')

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

# Initialize connection object
conn = init_connection()

# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# Get question solved by company
df = run_query("SELECT * from companies_solved")
st.dataframe(df, use_container_width=True)
