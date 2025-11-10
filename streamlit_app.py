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
with col2:
    # Placeholder for image
  st.image('https://raw.githubusercontent.com/asheana.juman/cis211_project1/refs/heads/main/funny cat.jfif', use_column_width=True)

# About Page
elif page == '😎 About':
  st. title ('About Me')

# Timeline of my professional Journey
 st.subheader('my journey 🗺')'

with st.expander('2025 - Present: Medgar Evers College'):
  st.write('''
            - Major: Business Admin
            - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
                - Activities: 
            ''')

st.expander('2023 - 2025: Epic South High School')
 st.write('''
                - Graduated with honors
                - AP Computer Science A (Score: 5)
                - Founded Coding Club
            ''')


  st.subheader('Interests & Hobbies 🏀')
  interests = ['Web Development', 'AI/Machine Learning', 'Photography', 'Basketball', 'Travel', 'Baseball']

  # Display the interests in columns
cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
  
