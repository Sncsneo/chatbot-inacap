import streamlit as st
from llama_index.core import VectorStoreIndex, Document, ServiceContext
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import fitz  # PyMuPDF
import random

# Obtén la API key de los secrets de Streamlit Cloud
openai_api_key = st.secrets["api_keys"]["OPENAI_API_KEY"]

def load_chatbot(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    
    document = Document(text=text)
    
    # Crea las instancias de OpenAI y OpenAIEmbedding usando la API key
    llm = OpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    embed_model = OpenAIEmbedding(api_key=openai_api_key)
    
    service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
    
    index = VectorStoreIndex.from_documents([document], service_context=service_context)
    return index.as_query_engine()

PREGUNTAS_EJEMPLO = [
    "¿Cuáles son los principales avances desde la última acreditación?",
    "¿Qué indicadores reflejan la calidad del CFT INACAP?",
    "¿Cómo se estructuran los mecanismos de aseguramiento de la calidad?",
    "¿Qué desafíos se identifican en el proceso de autoevaluación?",
    "¿Cuál es el rol del Modelo Educativo en la gestión institucional?",
]

def generar_pregunta_aleatoria(chatbot):
    return random.choice(PREGUNTAS_EJEMPLO)
