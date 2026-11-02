# P06 — Agentes confiables con Amazon Bedrock Mantle

## 🚀 Abrir en Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-04-ia-generativa/P06-agentes-confiables/P06_Velora_Agentes_Bedrock_Mantle.ipynb)

📋 [Leer el enunciado](./ENUNCIADO.md)

Al abrir el notebook en Colab, usa **Archivo → Guardar una copia en Drive** para conservar tus cambios.

## Requisito previo

Antes de ejecutar la práctica:

1. abre **Secrets** en Google Colab;
2. crea un secreto llamado `BEDROCK_API_KEY`;
3. pega una Amazon Bedrock API key válida;
4. habilita el acceso del notebook al secreto.

No escribas la clave directamente en una celda.

## Notebook

- `P06_Velora_Agentes_Bedrock_Mantle.ipynb`

## Tecnologías

- Amazon Bedrock Mantle
- OpenAI-compatible Responses API
- `openai.gpt-5.6-luna`
- `openai.gpt-oss-20b`
- client-side function calling

## Áreas

- comportamiento agéntico observable
- selección de tools
- least privilege
- indirect prompt injection desde tool responses
- proposal / approval / execution
- human-in-the-loop
- backend enforcement
- approvals de un solo uso
- `response_id` / `call_id`
- trazabilidad de proveedor y backend
- comparación opcional entre LLMs

Las dependencias específicas se instalan desde el propio notebook.
