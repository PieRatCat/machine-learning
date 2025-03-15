import streamlit as st

st.markdown(
    """
    <style>
    html, body {
        font-size: 18px;            
    }
    a {font-size: 20px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Define the pages
page_1 = st.Page("page_1.py", title="About project", icon=":material/home:")
page_2 = st.Page("page_2.py", title="App demo", icon=":material/draw:")

# Set up navigation
pg = st.navigation([page_1, page_2])

# Run the selected page
pg.run()