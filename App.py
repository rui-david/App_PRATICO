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
    

                    

