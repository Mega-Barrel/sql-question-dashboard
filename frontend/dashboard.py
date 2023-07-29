""" streamlit_app.py"""

import streamlit as st

st.set_page_config(
    page_title="SQL Question Tracker",
    page_icon='🎯',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://github.com/Mega-Barrel/sql-question-dashboard/issues",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


conn = st.experimental_connection(
    "sql_dashboard",
    type="sql"
)

df = conn.query("SELECT * FROM daily_solved ORDER BY created_at DESC")
st.dataframe(df)