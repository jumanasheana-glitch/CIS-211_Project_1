import streamlit as st 
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
  page_title = 'Asheana Juman | Portfolio',
  page_icon='🎯',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font_size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True) 

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '🤠 About', '💼 Projects', '🛠 Skills', '📄 Resume', '📩 Contact'])

# Home Page
if page == '🏠 Home':
 st.markdown('<p class="main-header">Asheana Juman</p>', unsafe_allow_html=True)
 st.markdown('<p class="sub-header">Aspiring Business Professional | Medgar Evers College</p>',unsafe_allow_html=True)

# Three Columns for stats
col1, col2, col3 = st.columns (3)

with col1:
    st.metric('GPA', '3,0', '📗')
with col2:
    st.metric('Projects', '5','💻')
with col3:
    st.metric('Skills', '10+', '🚀')

st.write('---')

 # Introduction with columns
col1, col2 = st.columns([2,1])
with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                
                I am a student that currently attending Medagr Evers College. Who's currently learning HTML, CSS, Javascript, and Python to build innovative solutions.
               
                🎯 **Current Focus:** Building interactive web applications with Streamlit
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
                🌱 **Fun Fact:** I can love doing cool makeup looks !
            ''')
