# P01 — Construcción y evaluación del modelo base

Laboratorio basado en el caso **Velora Finance**.

## Archivos

- `ENUNCIADO.md`
- `P01_Velora_Modelo_Base.ipynb`
- `../../data/velora_credit.csv.gz`

## Contenido

- carga y revisión del dataset;
- separación train/test;
- entrenamiento de un primer modelo de riesgo de crédito;
- matriz de confusión;
- accuracy;
- precision;
- recall;
- F1;
- ROC-AUC;
- PR-AUC;
- probabilidades y threshold;
- comparación de falsos positivos y falsos negativos;
- revisión de errores concretos del modelo.

## Variables del modelo

Predictores utilizados en P01:

```text
age
annual_income
debt_ratio
employment_months
late_payments_12m
credit_history_months
existing_debt
requested_amount
savings_balance
```

No se utilizan como predictores:

```text
application_id
customer_group
default
```

`default` es la variable objetivo.

## Dataset

El dataset incluido contiene 3.000 solicitudes sintéticas y se genera de forma reproducible con semilla `42` mediante:

```bash
python resources/generate_velora_credit.py
```

El fichero generado es:

```text
data/velora_credit.csv.gz
```

## Estado

✅ Enunciado y notebook del alumno preparados.

Pendiente:

- solución del instructor.
