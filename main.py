import streamlit as st
from chatbot_engine import load_chatbot, generar_pregunta_aleatoria

st.set_page_config(page_title="Chatbot Acreditación CFT INACAP")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = load_chatbot("documentos/Informe-cft-inacap-2024.pdf")

st.title("🤖 Chatbot Acreditación CFT INACAP 2024")

user_input = st.text_input("Escribe una pregunta o deja el campo vacío para una pregunta aleatoria")

if st.button("Consultar"):
    pregunta = user_input or generar_pregunta_aleatoria(st.session_state.chatbot)
    respuesta = st.session_state.chatbot.query(pregunta)
    st.write(f"**Pregunta:** {pregunta}")
    st.write(f"**Respuesta:** {respuesta.response}")
