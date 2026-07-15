from src.agent import ask

print("=" * 60)
print("OCI KNOWLEDGE ASSISTANT")
print("=" * 60)

while True:

    question = input("\nPregunta (escribe 'salir' para terminar): ")

    if question.lower() == "salir":
        break

    answer = ask(question)

    print("\nRespuesta:\n")
    print(answer)