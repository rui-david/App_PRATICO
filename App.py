import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.header("Introduzindo elementos Streamlit")
menu = option_menu(menu_title="Menu", 
                   options=["Inicio", "Gráficos Estáticos", "Gráficos Dinâmicos", "widgets", "Formulário"],
                   icons=["house", "bar-chart-line", "toggles", "bar-chart"],
                   menu_icon="cast",
                   default_index=0,
                   orientation="horizontal")

with st.sidebar:
    st.success("**UPLOAD DE DADOS**")

    dados = st.file_uploader(
      "Carregue...",
      type=["xlsx", "xls"]
    )
    if dados:
        def carregar_dados(dados):
            try:
                df = pd.read_excel(dados)
                return df
            except FileNotFoundError:
              return pd.DataFrame()

        df = carregar_dados(dados)
        st.table(df)

    else:
      st.info("carregue um ficheiroExcel para começar")

if menu == "Inicio":
  with st.expander("**Sobre o Instrituto Nacional de Estatistica**"):
    st.write("Acesse o site www.ine.cv")
    st.image("Logo-INE.png")

if menu == "Widgets":
  bt = st.button("Dê um clique")

  if bt: 
    st.info("clicaste num botão acima!")

  sd = st.slider("Mova o ponto do slide!", min_value=25, \
                 max_value=35, value=30, step=1
                 )
  texto = f"Eu tenho {sd} anos!"
  st.success(texto)
    

                    

