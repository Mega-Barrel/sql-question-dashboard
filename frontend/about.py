"""About Page"""

def about_page(st):
    """
    About Page for streamlit App
    """
    st.subheader('Welcome to my Streamlit App!')
    st.write('**Front End**')
    st.text(
        'This section serves as the front end of my Notion API Data Pipeline.'
    )
    st.text(
        'The app displays my daily progress in solving SQL problems from various platforms such as LeetCode, StrataScratch, and more.'
    )

    st.write('**BackEnd**')
    st.text('The backend of the app establishes a connection to the Notion API. Notion API is a powerful tool that enables seamless integration of Notion ')
    st.text('The backend runs daily cron jobs to receive and process new data from the Notion API, subsequently saving it to a database.')

    st.write('**Notion**')
    st.text('Notion API empowers developers to integrate Notion with external services, automate tasks, and build custom applications using programming languages like JavaScript, and Python.')
    st.text('By leveraging the capabilities of the Notion API, developers can create customized dashboards, automate tasks, and build powerful applications, all while fetching my daily SQL progress.')
