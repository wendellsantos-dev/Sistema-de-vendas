import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Sistema de vendas', page_icon='📊', layout='wide')
st.write('# Sistema de vendas')

tabela = pd.read_csv('vendas.csv')