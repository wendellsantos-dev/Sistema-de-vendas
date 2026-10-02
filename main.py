import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Sistema de vendas', page_icon='📊', layout='wide')
st.write('# Sistema de vendas')

tabela = pd.read_csv('vendas.csv')

with st.sidebar.form(key="Form_cadastro_venda"):
    st.write("## Cadastrar venda")
    data = st.date_input("Data")
    vendedor = st.selectbox("Vendedor", ["Ana", "Bruno", "Carla", "Pedro"])
    produto = st.selectbox("Produto", ["Notebook", "celular", "Fone"])
    quantidade = st.number_input("Quantidade", step=1, min_value=1)
    valor = st.number_input("Valor", min_value=0.0)
    botao_cadastrar = st.form_submit_button("Cadastrar venda")

if botao_cadastrar:
    nova_venda = [data, vendedor, produto, quantidade, valor]
    tabela.loc[len(tabela)] = nova_venda
    tabela.to_csv('vendas.csv', index= False)   
    st.success('Venda cadastrada!')