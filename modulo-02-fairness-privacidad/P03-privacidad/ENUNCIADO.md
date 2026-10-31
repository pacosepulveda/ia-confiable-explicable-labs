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

Modifica:

```python
TARGET_EPSILON
```

El entrenamiento privado utiliza Opacus con:

- DP-SGD;
- clipping por ejemplo;
- ruido calibrado;
- `TARGET_DELTA = 1e-5`;
- `MAX_GRAD_NORM = 1.0`;
- contabilidad PRV del presupuesto de privacidad.

## Parte 4 — Configuración efectiva de privacidad

Revisa los parámetros que producen la garantía:

- `target_epsilon`;
- `target_delta`;
- número de epochs;
- batch size;
- sampling rate aproximado;
- `noise_multiplier`;
- `max_grad_norm`.

Analiza por qué `epsilon` no debe interpretarse como un parámetro aislado.

## Parte 5 — Consumo de presupuesto durante el entrenamiento

Ejecuta el entrenamiento privado y revisa:

- loss por epoch;
- epsilon acumulado por epoch;
- gráfico de consumo del presupuesto.

Relaciona el número de pasos de optimización con la evolución del presupuesto.

## Parte 6 — Privacidad y utilidad

Compara entre el modelo convencional y el privado:

- ROC-AUC;
- accuracy;
- recall de impagos;
- epsilon realmente consumido.

Prueba, por ejemplo:

- `epsilon = 1`;
- `epsilon = 3`;
- `epsilon = 8`.

Compara también cómo cambia `noise_multiplier`.

## Parte 7 — Conexión con fairness

Compara por `customer_group`:

- recall de impagos;
- ROC-AUC.

Analiza si la pérdida de utilidad introducida por DP-SGD afecta de la misma forma a todos los grupos.

## Parte 8 — Composición y ciclo de vida

Modifica:

```python
EPSILON_POR_ENTRENAMIENTO
NUM_REENTRENAMIENTOS
```

Observa la cota de composición secuencial básica para `epsilon` y `delta`.

Distingue entre:

- población solapada;
- conjuntos realmente disjuntos;
- múltiples modelos, consultas o reentrenamientos durante el ciclo de vida.

## Parte 9 — Federated Learning

Revisa la comparación conceptual con Federated Learning.

Identifica por qué:

- evitar centralizar datos brutos no equivale a obtener Differential Privacy;
- las actualizaciones del modelo también pueden filtrar información;
- FL y DP son técnicas complementarias y no intercambiables.

## Resultado a conservar

Al terminar la práctica, conserva:

- métricas del modelo convencional;
- configuración efectiva del mecanismo DP;
- evolución de epsilon por epoch;
- `(epsilon, delta)` final;
- métricas del modelo DP-SGD;
- comparación de utilidad por grupo;
- escenario de composición seleccionado;
- conclusión razonada sobre el trade-off privacidad / utilidad y su gobierno.
