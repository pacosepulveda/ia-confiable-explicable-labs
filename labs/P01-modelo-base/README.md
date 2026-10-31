# P01 — Construcción y evaluación del modelo base

Laboratorio basado en el caso **Velora Finance**.

## Archivos

- `ENUNCIADO.md`
- `P01_Velora_Modelo_Base.ipynb`
- `../../resources/generate_velora_credit.py`

## Contenido

- carga y revisión del dataset;
- separación train/test;
- entrenamiento de un modelo base de riesgo de crédito;
- probabilidades y threshold;
- matriz de confusión;
- accuracy;
- precision;
- recall;
- F1;
- comparación de thresholds;
- falsos positivos y falsos negativos;
- revisión de errores concretos;
- ROC-AUC, Average Precision y Precision-Recall como extensión.

## Notebook

`P01_Velora_Modelo_Base.ipynb` contiene el código completo y las explicaciones necesarias para interpretar cada bloque y sus resultados. El alumno puede ejecutar la práctica de principio a fin sin escribir código.

La única modificación propuesta durante la práctica es cambiar el valor de `THRESHOLD_ELEGIDO` para comparar el efecto de distintos umbrales.

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

El dataset contiene 3.000 solicitudes sintéticas y se genera de forma reproducible con semilla `42` mediante `resources/generate_velora_credit.py`.

## Estado

✅ Notebook guiado y ejecutable preparado.
