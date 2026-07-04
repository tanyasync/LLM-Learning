import streamlit as st

st.title("Layout a page")
st.sidebar.header("Settings")
model = st.sidebar.selectbox("Model",["llama", "Openai", "Gemini"])
temperature = st.sidebar.slider("Temperature",0.0,1.0,0.2,0.05)
st.write(f"You picked **{model}** at temp:{temperature}")
st.header("welcome to new page")

st.header("Cols puts things side by side")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Col 1 Content")
    st.metric("Users",1290,+120)  
with col2:
    st.write("Col 2 Content")
    st.metric("Active Today",342,-8)   
with col3:
    st.write("Col 3 Content")
    st.metric("Signups",57,+15)

st.divider()
st.header("Tabs Act like mini page")
tab_summary, tab_details = st.tabs(["Summary","Details"])
with tab_summary:
    st.write("This is summary tab")
with tab_details:
    st.write("This is details tab")
    
st.header("Expander hides long or optional content")
with st.expander("Click to see content"):
    st.code(
        "You are a helpfull assistant",
        language = "text"
    )
show_debug = st.sidebar.checkbox("Show Debug Info")
if show_debug:
    st.warning("Debug Mode is ON")
    st.json({"Model":model,"Temperature":temperature})
    