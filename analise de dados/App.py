import streamlit as st
import pandas as pd
import plotly.express as px

#Criação de Titulo
st.title("Dashboard de desempenho de Alunos")

#Carregamento dos Dados
df = pd.read_csv("dados.csv")
st.subheader("Tabela de Dados")
st.dataframe(df)

#Criação de Filtro
Curso = st.selectbox("Selecione o Curso" ,df["Curso"].unique())
df_filtrado = df[df["Curso"] == Curso]
st.subheader("Dados filtrados")
st.write(df_filtrado)

#Elaboração de Grafico

barra = px.bar(
        df_filtrado,
        x= "Aluno",
        y= "Nota",
        color= "Aluno",
        title= "Notas dos alunos"
)
st.plotly_chart(barra)