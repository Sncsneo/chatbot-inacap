
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms import OpenAI
import os
import random

def load_chatbot(pdf_path):
    documents = SimpleDirectoryReader(input_files=[pdf_path]).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine(llm=OpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY")))

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
