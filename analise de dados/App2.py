import streamlit as st
import pandas as pd
import plotly.express as px

#Criação de Titulo
st.title("Dashboard Empresa")

#Carregamento dos Dados
df = pd.read_csv("novos_dados.csv")
st.subheader("tabela de dados")
st.dataframe(df)

#Criação de Filtro
departamento = st.selectbox("Selecione o departamento" ,df["departamento"].unique())
df_filtrado = df[df["departamento"] == departamento]
st.subheader("dados filtrados")
st.write(df_filtrado)

#Elaboração de Grafico

barra = px.bar(
        df_filtrado,
        x= "nome_completo",
        y= "salario_mensal_brl",
        color= "nome_completo",
        title= "funcionarios"
)
st.plotly_chart(barra)