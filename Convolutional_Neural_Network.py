import streamlit as st
from streamlit.components import v1 as components

st.set_page_config(layout="wide")

# Load HTML file
with open('Convolutional_Neural_Network_1.html', 'r') as file:    
    html_content = file.read()

components.html(html_content, width = None, height=1100)



# Load part 2
with open('Convolutional_Neural_Network_2.html', 'r') as file:    
    html_content_2 = file.read()

components.html(html_content_2, width = None, height=5500)