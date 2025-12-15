import streamlit as st
from streamlit_option_menu import option_menu
st.header("Introduzindo elementos Streamlit")
menu = option_menu(menu_title="Menu", 
                   options=["Inicio", "Gráficos Estáticos", "Gráficos Dinâmicos", "widgets", "Formulário"]
                   icons=["house", "bar-chart-line", "toggles", "bar-chart"],
                   menu_icon="cast",
                   default_index=0,
                   orientation="Horizontal"


                    

