import streamlit as st
from streamlit_option_menu import option_menu
from modulos.proprietarios import proprietarios
from modulos.usuarios import usuarios
from modulos.carros import carros
from modulos.inicio import inicio

st.set_page_config(layout="wide")

with st.sidebar:
    opcao = option_menu("Carford", ["Inicio", "Proprietários", "Carros", "Usuarios"],
                         icons=['house', 'arrow-up', 'arrow-down', 'people'],
                         menu_icon="currency-dollar", default_index=0)

if opcao == "Inicio":
    inicio()

if opcao == "Proprietários":
    proprietarios()

if opcao == "Carros":
    carros()

if opcao == "Usuarios":
    usuarios()
