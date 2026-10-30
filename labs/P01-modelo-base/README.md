# P01 — Construcción y evaluación del modelo base

Laboratorio basado en el caso **Aurea Finance**.

## Datos

Generar el dataset desde la raíz del repositorio:

```bash
python resources/generate_aurea_credit.py
```

Se crea:

```text
data/aurea_credit.csv.gz
```

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
- análisis de falsos positivos y falsos negativos.

## Variables del modelo en P01

Se utilizarán como predictores:

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

No se utilizarán como predictores:

```text
application_id
customer_group
default
```

`default` es la variable objetivo.

## Estado

🚧 **En preparación.**

Pendiente de añadir:

- enunciado definitivo;
- notebook del alumno;
- solución del instructor.
