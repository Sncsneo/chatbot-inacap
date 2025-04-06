from llama_index.core import VectorStoreIndex, Document, ServiceContext
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.llms import OpenAI
import os
import fitz  # PyMuPDF
import random

def load_chatbot(pdf_path):
    # Leer el contenido del PDF con PyMuPDF
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()

    document = Document(text=text)

    llm = OpenAI(model="gpt-3.5-turbo")
    embed_model = OpenAIEmbedding()
    service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)

    index = VectorStoreIndex.from_documents([document], service_context=service_context)
    return index.as_query_engine()

PREGUNTAS_EJEMPLO = [
    "¿Qué avances se han logrado en la dimensión de Vinculación con el Medio?",
    "¿Cómo se estructura el Modelo Educativo del CFT INACAP?",
    "¿Qué acciones se tomaron luego de la última acreditación en 2018?",
    "¿Qué indicadores reflejan la empleabilidad de los titulados del CFT?",
    "¿Qué debilidades se identificaron en el proceso de autoevaluación?",
    "¿Cuáles son los objetivos del Plan Estratégico 2025-2030?"
]

def generar_pregunta_aleatoria(chatbot):
    return random.choice(PREGUNTAS_EJEMPLO)
