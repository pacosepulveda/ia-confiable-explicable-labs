# P03 — Differential Privacy con PyTorch y Opacus

## Escenario

Velora Finance quiere entrenar un modelo de riesgo reduciendo la influencia observable de cada registro individual en el modelo publicado.

La práctica compara un entrenamiento convencional con el mismo tipo de modelo entrenado mediante **DP-SGD**.

## Parte 1 — Preparación

Activa una GPU T4 en Google Colab si está disponible.

Instala:

```text
opacus==1.6.0
```

El notebook detecta automáticamente si existe GPU.

## Parte 2 — Dataset y modelo

Genera una cohorte sintética de 30.000 solicitudes utilizando el mismo generador de Velora Finance.

Prepara las mismas variables predictoras utilizadas en P01 y P02.

Entrena primero un modelo PyTorch convencional y conserva sus métricas de referencia.

## Parte 3 — Entrenamiento privado

Modifica únicamente:

```python
TARGET_EPSILON
```

El entrenamiento privado utiliza Opacus con:

- DP-SGD;
- clipping por ejemplo;
- ruido calibrado;
- contabilidad del presupuesto de privacidad;
- `TARGET_DELTA = 1e-5`.

Compara el `epsilon` realmente gastado con el valor objetivo.

## Parte 4 — Privacidad y utilidad

Compara entre el modelo convencional y el privado:

- ROC-AUC;
- accuracy;
- recall de impagos.

Prueba, por ejemplo:

- `epsilon = 1`;
- `epsilon = 3`;
- `epsilon = 8`.

Analiza cómo cambia la utilidad al modificar la garantía de privacidad.

## Parte 5 — Conexión con fairness

Compara por `customer_group`:

- recall de impagos;
- ROC-AUC.

Analiza si la pérdida de utilidad introducida por DP-SGD afecta de la misma forma a todos los grupos.

## Parte 6 — Federated Learning

Revisa la comparación conceptual con Federated Learning.

Identifica por qué:

- evitar centralizar datos brutos no equivale a obtener Differential Privacy;
- las actualizaciones del modelo también pueden filtrar información;
- FL y DP son técnicas complementarias y no intercambiables.

## Resultado a conservar

Al terminar la práctica, conserva:

- métricas del modelo convencional;
- `(epsilon, delta)` del entrenamiento privado;
- métricas del modelo DP-SGD;
- comparación de utilidad por grupo;
- conclusiones sobre el trade-off privacidad / utilidad.
