""" streamlit_app.py"""

import streamlit as st

# Import for pages
from frontend.about import about_page
from frontend.graphs import line_chart_, pie_chart_, bar_chart_
from frontend.raw_data import raw_table, clean_table

st.set_page_config(
    page_title="SQL Question Tracker",
    page_icon='🎯',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://github.com/Mega-Barrel/sql-question-dashboard/issues",
        'About': "# This is a header. This is an *extremely* cool app!"
    },
    layout='wide'
)

@st.cache_resource()
def get_connection():
    """
    SQLite experimental connection
    """
    conn = st.experimental_connection('daily_sql_tracker', type='sql')
    return conn

# Set title
st.title('Daily SQL Question Tracker')

# Streamlit Tabs
about, graphs, raw_data = st.tabs([
    'About',
    'Graphs',
    'Raw Data'
])

with about:
    with st.chat_message('assistant', avatar='🤖'):
        st.write('Hey Bot, please share some insignts regarding this App.')
        about_page(st)

with graphs:
    with st.chat_message('user'):
        st.write("Daily Question Solved 📈")
        line_chart_(st, get_connection())

    # Specify 2 column
    col1, col2 = st.columns(2)
    
    with col1.chat_message('user'):
        st.write("Question Solved | Difficulty % 🎯")
        pie_chart_(col1, get_connection())
    
    with col2.chat_message('user'):
        st.write("Question Solved | Company 🏢")
        bar_chart_(col2, get_connection())

with raw_data:
    with st.chat_message("user"):
        st.write("Raw Data 📔")
        raw_table(st, get_connection())
    
    with st.chat_message("user"):
        st.write("Transformed Data 📖")
        clean_table(st, get_connection())


st.markdown(
        """
        <style>
            .footer a {
                text-decoration: none;
            }
            </style>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
        ---
        <div class="footer">
            <p>Created with ❤️ by <a href="https://github.com/Mega-Barrel/">Saurabh Joshi</a> | Powered by <a href="https://www.streamlit.io/">Streamlit</a> | <a href="https://developers.notion.com/">Notion API </a></p>
            <p>Follow me on <a href="https://www.linkedin.com/in/saurabhJoshi2403">LinkedIn</a> | Connect on <a href="https://twitter.com/Saurabh___Joshi">Twitter</a></p>
        </div>
    """,
    unsafe_allow_html=True
)