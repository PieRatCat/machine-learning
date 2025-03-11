import streamlit as st


if "option" in st.session_state:
    st.session_state.option = st.session_state.option

if "color" in st.session_state:
    st.session_state.color = st.session_state.color

if "name" in st.session_state:
    st.session_state.name = st.session_state.name
 

# Define the pages
page_1 = st.Page("page_1.py", title="Page 1", icon="📗")
page_2 = st.Page("page_2.py", title="Page 2", icon="📘")
page_3 = st.Page("page_3.py", title="Page 3", icon="📙")

# Set up navigation
pg = st.navigation([page_1, page_2, page_3])

# Run the selected page
pg.run()