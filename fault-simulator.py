import streamlit as st
import streamlit.components.v1 as components

# Configure the Streamlit page to use the full width
st.set_page_config(
    page_title="Fault Lab Interactive",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Read and embed the HTML file verbatim
try:
    with open("Fault-Lab-Interactive.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # Render the HTML component
    # height is set to simulate a standard desktop viewport; scrolling enabled for overflow
    components.html(html_content, height=900, scrolling=True)

except FileNotFoundError:
    st.error("Error: Could not find 'Fault-Lab-Interactive.html'. Please make sure the file is in the exact same directory as this app.py script.")