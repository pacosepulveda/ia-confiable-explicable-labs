# IA Confiable y Explicable — Laboratorios

Repositorio de prácticas del curso **Inteligencia Artificial Confiable y Explicable**.

Los laboratorios están organizados por módulo y siguen un caso común basado en **Velora Finance**. Cada práctica incluye un enunciado y uno o varios notebooks preparados para trabajar durante la formación.

## 🚀 Abrir los notebooks en Google Colab

Los notebooks pueden abrirse directamente desde GitHub en Google Colab. **No es necesario descargarlos ni subirlos manualmente.**

Flujo recomendado:

1. Lee el `ENUNCIADO.md` de la práctica.
2. Pulsa **Open in Colab**.
3. En Colab, usa **Archivo → Guardar una copia en Drive** para conservar tus cambios.
4. Trabaja sobre tu copia personal.

> El notebook original permanece en GitHub. Los cambios realizados por el alumno en Colab no modifican este repositorio.

| Práctica | Tema | Colab |
|---|---|---|
| P01 | Modelo base | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-01-fundamentos/P01-modelo-base/P01_Velora_Modelo_Base.ipynb) |
| P02 | Fairness | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-02-fairness-privacidad/P02-fairness/P02_Velora_Fairness.ipynb) |
| P03 | Differential Privacy | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-02-fairness-privacidad/P03-privacidad/P03_Velora_Privacidad.ipynb) |
| P04A | Explicabilidad tabular | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-03-explicabilidad/P04-explicabilidad/P04A_Velora_Explicabilidad_Tabular.ipynb) |
| P04B | Saliency y visión | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-03-explicabilidad/P04-explicabilidad/P04B_Saliency_Vision.ipynb) |
| P05 | RAG confiable | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-04-ia-generativa/P05-rag-confiable/P05_Velora_RAG_Confiable.ipynb) |
| P06 | Agentes confiables | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-04-ia-generativa/P06-agentes-confiables/P06_Velora_Agentes_Bedrock_Mantle.ipynb) |
| P07 | Auditoría end-to-end | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-05-gobernanza-auditoria/P07-auditoria-end-to-end/P07_Velora_Auditoria_End_to_End.ipynb) |

### Requisitos especiales

- **P03**: se recomienda activar una GPU T4 en Colab.
- **P05**: requiere GPU T4 para ejecutar el LLM local con una experiencia razonable.
- **P06**: requiere un secreto de Colab llamado `BEDROCK_API_KEY`, tal como se explica dentro del notebook.

## Módulos y prácticas

| Módulo | Prácticas |
|---|---|
| [M01 — Fundamentos de IA confiable](./modulo-01-fundamentos/) | [P01 — Construcción y evaluación del modelo base](./modulo-01-fundamentos/P01-modelo-base/) |
| [M02 — Fairness, sesgos y privacidad](./modulo-02-fairness-privacidad/) | [P02 — Auditoría de fairness con Fairlearn](./modulo-02-fairness-privacidad/P02-fairness/) · [P03 — Differential Privacy con PyTorch y Opacus](./modulo-02-fairness-privacidad/P03-privacidad/) |
| [M03 — Explicabilidad](./modulo-03-explicabilidad/) | [P04 — Explicabilidad tabular y visión](./modulo-03-explicabilidad/P04-explicabilidad/) |
| [M04 — IA generativa confiable](./modulo-04-ia-generativa/) | [P05 — RAG confiable](./modulo-04-ia-generativa/P05-rag-confiable/) · [P06 — Agentes confiables](./modulo-04-ia-generativa/P06-agentes-confiables/) |
| [M05 — Gobernanza y auditoría](./modulo-05-gobernanza-auditoria/) | [P07 — Auditoría end-to-end](./modulo-05-gobernanza-auditoria/P07-auditoria-end-to-end/) |

## Cómo trabajar con las prácticas

Los notebooks están preparados para reducir el código accesorio y centrar el trabajo en la toma de decisiones, la experimentación y el análisis de resultados. Las dependencias específicas se instalan desde el propio notebook cuando son necesarias.

## Datos y recursos compartidos

- [`data/`](./data/) — Información sobre el dataset sintético de Velora Finance.
- [`resources/`](./resources/) — Utilidades compartidas, incluido el generador reproducible del dataset.
