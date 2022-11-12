import streamlit as st

st.title("這是主要的標題")

with st.sidebar:
    st.header("這是我的sidebar")
    button = st.button("Say Hello")
    if button:
        st.write('Why hello there')
    else:
        st.write('Goodbye')