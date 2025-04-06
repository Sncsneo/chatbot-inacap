from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import ServiceContext
import os
import random

def load_chatbot(pdf_path):
    documents = SimpleDirectoryReader(input_files=[pdf_path]).load_data()
    embed_model = OpenAIEmbedding()
    service_context = ServiceContext.from_defaults(embed_model=embed_model)
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
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
