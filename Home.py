import streamlit as st
import pandas as pd


from app.db import conn
from app.cyber_incidents import get_cyber_incidents, migrate_cyber_incidents_table

df = get_cyber_incidents(conn)
 
st.set_page_config(
    page_title='My app',
    page_icon='👋',
    layout='wide'
)
 
 
st.title("📊 Sales Dashboard")
with st.sidebar:
    st.header('Control')
    year = st.selectbox('Year', ['Low', 'Medium', 'High'])
    
 
#filter = df[(df['severity'] == year)]
 
col1, col2 = st.columns(2)
 
with col1:
    st.subheader('Left')
    st.bar_chart(x='timestamp', y='incident_id', data=df)
 
with col2:
    st.subheader('Right')
    st.line_chart(x='status', y='incident_id', data=df)
 
 
with st.expander('See details'):
    st.write('Hidden content')
    st.dataframe(df)