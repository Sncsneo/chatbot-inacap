
import streamlit as st
from chatbot_engine import load_chatbot, generar_pregunta_aleatoria
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Chatbot Acreditación INACAP", layout="wide")
st.title("🤖 Chatbot de Estudio - Acreditación CFT INACAP")

if "chatbot" not in st.session_state:
    with st.spinner("Cargando el informe y creando el índice..."):
        st.session_state.chatbot = load_chatbot("documentos/Informe-cft-inacap-2024.pdf")

user_input = st.text_input("Escribe tu pregunta sobre el informe:")

col1, col2 = st.columns(2)

if col1.button("❓ Preguntar") and user_input:
    with st.spinner("Buscando respuesta..."):
        response = st.session_state.chatbot.query(user_input)
        st.write(response.response)

if col2.button("🧪 Evaluarme con una pregunta aleatoria"):
    with st.spinner("Generando pregunta..."):
        pregunta = generar_pregunta_aleatoria(st.session_state.chatbot)
        st.session_state.pregunta_actual = pregunta
        st.write("💬 **Pregunta del informe:**")
        st.write(pregunta)

if "pregunta_actual" in st.session_state:
    respuesta_usuario = st.text_area("✍️ Escribe tu respuesta aquí:")
    if st.button("✅ Evaluar mi respuesta"):
        with st.spinner("Analizando tu respuesta..."):
            retro = st.session_state.chatbot.query(
                f"Evalúa la siguiente respuesta respecto a esta pregunta:\n\n"
                f"Pregunta: {st.session_state.pregunta_actual}\n"
                f"Respuesta: {respuesta_usuario}\n"
                f"Usa el informe como fuente para verificar si es correcta."
            )
            st.write("📝 **Retroalimentación:**")
            st.write(retro.response)
