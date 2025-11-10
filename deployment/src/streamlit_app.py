import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title='Heart Disease Prediction',
    layout='wide',
    initial_sidebar_state='expanded'
)

page = st.sidebar.selectbox('Pilih Page :', ('EDA', 'Prediction'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()
