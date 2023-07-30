"""Raw Data"""

def raw_table(st, conn):
    """
    Method to generate Streamlit dataframe for raw_data table
    """
    daily_solved = conn.query(
        '''
            SELECT
                *
            FROM
                raw_data
            ORDER BY
                created_at ASC
        '''
    )
    st.dataframe(daily_solved, use_container_width=True, hide_index=True)

def clean_table(st, conn):
    """
    Method to generate Streamlit dataframe for transformed table
    """
    df1, df2, df3 = st.columns(3)
    
    df1_query = conn.query('SELECT * FROM daily_solved')
    df2_query = conn.query('SELECT * FROM companies_solved')
    df3_query = conn.query('SELECT * FROM ques_difficulty')

    df1.write('Daily Solved Table')
    df1.dataframe(df1_query, use_container_width=True, hide_index=True)

    df2.write('Companies Solved Table')
    df2.dataframe(df2_query, use_container_width=True, hide_index=True)

    df3.write('Question Difficulty Table')
    df3.dataframe(df3_query, use_container_width=True, hide_index=True)
