"""Graphs Page"""
import plotly.express as px

def line_chart_(st, conn):
    """
    Method to generate plotly line chart
    """
    daily_solved = conn.query(
        '''
            SELECT
                *
            FROM
                daily_solved
            WHERE
                created_at BETWEEN datetime("now", "-90 days")
                AND
                datetime("now", "localtime")
            ORDER BY
                created_at ASC
        '''
    )
    fig = px.line(
        daily_solved,
        x = 'created_at',
        y = 'question_solved',
        text="question_solved"
    )
    fig.update_yaxes(
        rangemode="tozero"        
    )
    fig.update_traces(
        textposition="top center"
    )
    fig.update_traces(
        line_color='#0068c9'
    )
    st.plotly_chart(fig, use_container_width=True)

def pie_chart_(st, conn):
    """
    Method to generate plotly pie chart
    """
    difficulty_questions = conn.query('SELECT * FROM ques_difficulty')
    fig = px.pie(
        difficulty_questions, 
        values='question_solved', 
        names='difficulty',
        color='difficulty',
        color_discrete_map={
            'Easy':'#0068c9',
            'Medium':'#83c9ff',
            'Hard': '#4597dc'
        }
    )
    fig.update_traces(
        hole=.4, 
        hoverinfo="label+percent+name"
    )
    st.plotly_chart(fig, use_container_width=True)

def bar_chart_(st, conn):
    """
    Method to generate plotly bar chart
    """
    top_10_companies = conn.query(
        """
            SELECT
                company,
                question_solved
            FROM
                companies_solved
            WHERE
                company <> 'N/A'
        """
    )
    fig = px.bar(
        top_10_companies, 
        y='question_solved', 
        x='company', 
        text_auto='s'
    )
    fig.update_traces(
        textfont_size=12, 
        textangle=1, 
        textposition="outside", 
        cliponaxis=False
    )
    fig.update_yaxes(
        rangemode="tozero"        
    )
    st.plotly_chart(fig, use_container_width=True)
