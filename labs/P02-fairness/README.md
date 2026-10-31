# P02 — Auditoría y mitigación de fairness

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
- tasa de aprobación, FPR y FNR;
- demographic parity difference / ratio;
- equal opportunity difference;
- equalized odds difference;
- sensibilidad de las métricas al threshold;
- calibración por grupo;
- separación train / calibración de mitigación / test final;
- mitigación mediante `ThresholdOptimizer`;
- comparación del sistema base y el mitigado;
- análisis de trade-offs y uso del atributo sensible en postprocesado.

## Variables

`customer_group` no se utiliza como predictor del modelo base. Se utiliza como atributo de auditoría y, en la fase de mitigación, como `sensitive_features` del postprocesador.

## Dependencias

- scikit-learn
- Fairlearn 0.15.0
- pandas
- NumPy
- Matplotlib

## Estado

✅ Notebook validado en Google Colab.
