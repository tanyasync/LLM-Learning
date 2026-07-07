import time 
import streamlit as st
st.title("caching:run slow work once, not every rerun")

def slow_uncached(n):
    time.sleep(2)
    return n*n

@st.cache_data
def slow_cached(n):
    time.sleep(2)
    return n*n

st.header("Uncached: Slow every single time")
number1 = st.slider("pick a No (Uncached)", 1,10,3)
if st.button("Square it (Uncached)"):
    result = slow_uncached (number1)
    st.success(f"{number1} squared is {result}")
    
st.divider()
st.header("cached: Slow once per value, then instant")
number2 = st.slider("Pick a number(cached)", 1,10,3)

if st.button ("Square it (cached)"):
    result = slow_cached(number2)
    st.success(f"{number2} squared is {result}")
    