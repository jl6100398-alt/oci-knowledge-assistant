from google import genai

from src.config import GOOGLE_API_KEY

from src.prompt import SYSTEM_PROMPT

from src.vectorstore_manager import VectorStoreManager


class OCIAgent:

    def __init__(self):

        self.client = genai.Client(
            api_key=GOOGLE_API_KEY
        )

        self.vectorstore = VectorStoreManager()

    def ask(self, question):

        docs = self.vectorstore.search(question)

        context = ""

        sources = set()

        for doc in docs:

            source = doc.metadata.get(
                "source",
                "Desconocido"
            )

            page = doc.metadata.get(
                "page",
                "?"
            )

            sources.add(
                f"{source} (Página {page})"
            )

            context += f"""

Documento:

{source}

Página:

{page}

Contenido:

{doc.page_content}

-----------------------------------

"""

        prompt = f"""
{SYSTEM_PROMPT}

==============================

CONTEXTO

==============================

{context}

==============================

PREGUNTA

==============================

{question}

==============================

RESPUESTA

==============================
"""

        response = self.client.models.generate_content(

            model="models/gemini-flash-latest",

            contents=prompt

        )

        answer = response.text

        answer += "\n\nFuentes utilizadas\n\n"

        for source in sorted(sources):

            answer += f"• {source}\n"

        return answer


agent = OCIAgent()


def ask(question):

    return agent.ask(question)