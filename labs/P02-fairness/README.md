# P02 — Auditoría de fairness

Laboratorio basado en el caso **Velora Finance**.

## Archivos

- `ENUNCIADO.md`
- `P02_Velora_Fairness.ipynb`
- `../../resources/generate_velora_credit.py`

## Contenido

- auditoría con Fairlearn 0.15.0;
- `MetricFrame`;
- métricas globales y desagregadas;
- tasas base por grupo;
- tasa de aprobación;
- falsos positivos y falsos negativos;
- demographic parity difference / ratio;
- equal opportunity difference;
- equalized odds difference;
- sensibilidad de las métricas al threshold;
- exclusión del atributo de grupo del modelo y auditoría posterior.

## Variables

`customer_group` se utiliza para auditoría y no como predictor del modelo.

El modelo utiliza las mismas variables predictoras de P01.

## Estado

✅ Notebook guiado y ejecutable.
