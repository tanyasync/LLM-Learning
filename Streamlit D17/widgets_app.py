import streamlit as st
st.title("widgets: input you can read")
st.header("Tell me about yourself!")
name = st.text_input("What is your name?","")
age = st.slider("How old are you?",0,100,20)
city = st.selectbox("Which city?",["Lko","Delhi","Mumbai","Pune"])
st.write(f"Hi **{name or 'friend'}**, age: {age},city: {city}")

st.divider()
st.header("Live Tip calculator")
bill = st.number_input("Bill amount (Rs)",min_value=0.0, value=500.0, step=50.0)
tip_percent = st.slider("Tip %", 0,30,10)
tip = bill * tip_percent / 100
total = bill + tip
st.metric("Total to pay", f"Rs{total:.2f}")
st.divider()
