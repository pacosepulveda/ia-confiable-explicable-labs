# P01 — Construcción y evaluación del modelo base

## Escenario

Velora Finance está preparando un sistema de apoyo a la evaluación de solicitudes de crédito.

La entidad dispone de un histórico sintético de solicitudes con información económica y financiera del solicitante. La variable `default` indica si la operación terminó en impago:

- `default = 0`: no hubo impago.
- `default = 1`: hubo impago.

En esta práctica se construirá un primer modelo de riesgo y se analizará su comportamiento antes de considerar cualquier uso operativo.

## Archivos

- `labs/P01-modelo-base/P01_Velora_Modelo_Base.ipynb`
- `resources/generate_velora_credit.py`

## Variables

Se utilizarán como predictores:

- `age`
- `annual_income`
- `debt_ratio`
- `employment_months`
- `late_payments_12m`
- `credit_history_months`
- `existing_debt`
- `requested_amount`
- `savings_balance`

No se utilizarán como predictores en esta práctica:

- `application_id`
- `customer_group`
- `default`

`default` es la variable objetivo.

## Parte 1 — Revisar los datos

1. Ejecuta la celda inicial para cargar el dataset.
2. Comprueba número de filas, columnas y tipos de datos.
3. Calcula la distribución de `default`.
4. Determina el porcentaje de operaciones que terminaron en impago.

Anota el resultado. No continúes suponiendo que las dos clases están equilibradas.

## Parte 2 — Preparar train y test

1. Construye `X` con las variables indicadas.
2. Construye `y` con `default`.
3. Divide el dataset:
   - 80% entrenamiento.
   - 20% test.
   - `random_state=42`.
   - utiliza `stratify=y`.
4. Comprueba que la tasa de impago es similar en ambos conjuntos.

## Parte 3 — Entrenar el modelo base

Construye un `Pipeline` con:

- `StandardScaler`
- `LogisticRegression(max_iter=1000, random_state=42)`

Entrena el modelo únicamente con `X_train` e `y_train`.

Obtén para el conjunto de test:

- la probabilidad estimada de impago;
- la predicción usando inicialmente `threshold = 0.5`.

## Parte 4 — Evaluar `threshold = 0.5`

Calcula:

- matriz de confusión;
- accuracy;
- precision;
- recall;
- F1;
- ROC-AUC;
- Average Precision (AP);
- PR-AUC, calculada como el área bajo la curva Precision-Recall.

A partir de la matriz de confusión identifica:

- verdaderos negativos;
- falsos positivos;
- falsos negativos;
- verdaderos positivos.

Responde:

1. ¿Qué porcentaje de impagos reales está detectando el modelo?
2. ¿Cuántas operaciones que terminarán en impago clasifica como no impago?
3. ¿La accuracy por sí sola describe bien el comportamiento del modelo?
4. En este escenario, ¿qué consecuencia tendría un falso negativo?
5. ¿Y un falso positivo?

## Parte 5 — Cambiar el threshold

Evalúa al menos estos valores:

```text
0.20
0.30
0.40
0.50
0.60
0.70
```

Para cada threshold calcula:

- accuracy;
- precision;
- recall;
- F1;
- falsos positivos;
- falsos negativos.

Construye una tabla comparativa.

Después responde:

1. ¿Qué ocurre con el recall cuando bajas el threshold?
2. ¿Qué ocurre con los falsos positivos?
3. ¿Qué ocurre cuando subes el threshold?
4. ¿Qué threshold obtiene la mayor accuracy?
5. ¿Coincide con el threshold que elegirías si el coste de conceder crédito a una operación que acabará en impago fuese elevado?
6. ¿Cambiarías tu elección si el coste principal fuese rechazar solicitudes solventes?

## Parte 6 — Curvas de evaluación

Representa:

- curva ROC;
- curva Precision-Recall.

Incluye:

- ROC-AUC;
- Average Precision (AP);
- PR-AUC;
- proporción de la clase positiva como referencia para interpretar la curva Precision-Recall.

## Parte 7 — Revisar errores concretos

Localiza en el conjunto de test:

- al menos un falso positivo;
- al menos un falso negativo.

Muestra sus datos originales junto con:

- `application_id`;
- probabilidad estimada de impago;
- predicción;
- valor real de `default`.

No intentes todavía explicar por qué el modelo ha producido esas probabilidades. Esa parte se tratará posteriormente.

## Resultado a conservar

Al terminar, conserva:

- el modelo entrenado;
- las probabilidades del conjunto de test;
- las predicciones;
- la tabla de thresholds.

Estos elementos se reutilizarán en prácticas posteriores.
