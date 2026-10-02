import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Sistema de vendas', page_icon='📊', layout='wide')
st.write('# Sistema de vendas')

tabela = pd.read_csv('vendas.csv')

st.sidebar.write('## Cadastrar venda')
data = st.sidebar.date_input('Data')
vendedor = st.sidebar.selectbox('Vendedor', ['Ana', 'Bruno', 'Carla', 'Pedro'])
produto = st.sidebar.selectbox('Produto'['Notebook', 'celular', 'Fone'])
quantidade = st.sidebar.number_input('Quantidae', step= 1)
valor = st.sidebar.number_input('Valor')
botao_cadastrar = st.sidebar.button('Cadastrar venda')