import streamlit as st

st.title("這是我的大標題")
st.header("這是次標題")
st.subheader("這是我的次次標題")
st.caption("這是caption")
x = 10
y = 20
st.caption(f"x={x},y={y}")
st.code('''
def hello():
    print("Hello! World")
''')

st.text('''
 ...-....
 ....-...
 .....-...
''')
