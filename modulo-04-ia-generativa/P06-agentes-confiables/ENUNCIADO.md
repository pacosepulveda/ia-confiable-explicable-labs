# P06 — Agentes confiables con Amazon Bedrock Mantle

## Escenario

Velora Finance quiere utilizar un agente capaz de consultar información y solicitar acciones mediante herramientas, manteniendo los controles de autorización fuera del LLM.

## Tareas

1. Cargar una Bedrock API key desde Colab Secrets.
2. Seleccionar `openai.gpt-5.6-luna` o `openai.gpt-oss-20b`.
3. Ejecutar una tarea con scope `read_only` y observar las rondas del agente.
4. Correlacionar `response_id`, `call_id` y audit log.
5. Analizar indirect prompt injection procedente de una tool response.
6. Comparar scope `read_only` y `controlled_write`.
7. Crear una propuesta sin producir side effects.
8. Emitir una aprobación humana fuera de las tools del agente.
9. Ejecutar únicamente la acción exacta autorizada.
10. Comprobar que la aprobación no puede reutilizarse.
11. Comparar opcionalmente los dos LLMs manteniendo constantes tarea, tools, permisos y backend.
12. Distinguir controles de prompt, permisos, validación backend y auditoría.
