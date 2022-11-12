import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("cat.png")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

col4, col5, col6 = st.columns(3)

with col4:
    st.header("A cat")
    st.image("cat.png")

with col5:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col6:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")