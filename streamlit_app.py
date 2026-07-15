import time
import streamlit as st

from src.agent import ask

st.set_page_config(
    page_title="OCI Knowledge Assistant",
    page_icon="☁",
    layout="wide"
)

# ----------------------------
# Inicializar historial
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.title("☁ OCI Assistant")

    st.markdown("---")

    st.info("4 documentos indexados")

    st.markdown("---")

    st.subheader("Documentos")

    st.write("📄 Conceptos básicos OCI")

    st.write("📄 Governance")

    st.write("📄 Networking")

    st.write("📄 Recursos y servicios OCI")

    st.markdown("---")

    if st.button("🗑 Limpiar conversación"):

        st.session_state.messages = []

        st.rerun()

# ----------------------------
# Encabezado
# ----------------------------

st.title("☁ OCI Knowledge Assistant")

st.markdown(
"""
Asistente inteligente especializado en Oracle Cloud Infrastructure (OCI).
"""
)

# ----------------------------
# Mostrar historial
# ----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ----------------------------
# Entrada del usuario
# ----------------------------

if prompt := st.chat_input("Escribe tu pregunta..."):

    # Mostrar mensaje del usuario

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # Respuesta

    with st.chat_message("assistant"):

        inicio = time.time()

        with st.spinner("Consultando documentación..."):

            respuesta = ask(prompt)

        fin = time.time()

        st.markdown(respuesta)

        st.caption(f"⏱ Tiempo: {fin-inicio:.2f} segundos")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": respuesta
        }
    )