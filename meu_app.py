import streamlit as st 
import pandas as pd

st.set_page_config(page_title="Meu site streamlit")

with st.container():
    st.subheader("Meu primeiro site com streamlit!")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Hashenco ao longo de maio")
    st.write("Quer aprender Python? [Clique aqui](https://www.google.com)")

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    qtd_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    num_dias = int(qtd_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")

