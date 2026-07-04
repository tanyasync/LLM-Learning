import streamlit as st
import pandas as pd

st.title("Ways to show content")
st.header("1.Text")
st.write("st.write prints plain text and supports **Markdown** also")
st.code("def greet(name):\n return f'Hi {name}'", language = "python")
st.divider()    
st.header("2. Data and tables")
student = pd.DataFrame(
    {
        "Name":["tanya", "jin", "jimin"],
        "city":["lko", "delhi", "mumbai"],
        "Score":[90, 80, 85]
        }
)
st.dataframe(student,width="stretch")
st.success("Success")
st.info("Info")
st.warning("Warning")
st.error("Error")

