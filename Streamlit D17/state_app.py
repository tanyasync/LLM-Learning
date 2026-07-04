import streamlit as st
#count = 0
#if st.button("Add One"):
#   count = count+1
#st.write("Count", count)


#st.session_state
if "count" not in st.session_state:
    st.session_state.count=0
if st.button("Add One"):
    st.session_state.count +=1
st.write("Count Value :", st.session_state.count)
