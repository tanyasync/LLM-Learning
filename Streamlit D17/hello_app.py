import streamlit as st
st.title("Hello, Streamlit!")
st.header("I am a webpage written in python")
st.subheader("No HTML. No CSS. No JavaScript.")
st.write("the whole page is just python")
st.write("two plus two is:", 2+2)
st.markdown("Streamlit understands **Markdown**")
st.button("Click me")
if st.button("Click here"):
    st.success("Button was clicked")