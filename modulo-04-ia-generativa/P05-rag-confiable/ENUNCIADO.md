# P05 — RAG confiable

## Escenario

Velora Finance quiere desplegar un asistente interno capaz de responder preguntas sobre políticas y procedimientos utilizando una base documental.

## Tareas

1. Generar chunks con diferentes tamaños y overlap.
2. Crear embeddings e índice FAISS.
3. Evaluar retrieval mediante Hit@K y MRR.
4. Comparar una respuesta del LLM sin RAG y con RAG.
5. Exigir citas y comprobar que proceden de fuentes recuperadas.
6. Probar una pregunta sin evidencia y observar la abstención.
7. Analizar un indirect prompt injection almacenado en el corpus.
8. Comparar el contexto sin filtrar y el modo endurecido.
9. Identificar las evidencias mínimas necesarias para auditar una respuesta RAG.
