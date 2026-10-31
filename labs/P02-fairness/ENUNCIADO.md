# P02 — Auditoría de fairness con Fairlearn

## Escenario

En P01 se evaluó globalmente el modelo de riesgo de Velora Finance.

En esta práctica se reutilizan el mismo dataset, la misma partición train/test y el mismo modelo para analizar su comportamiento por `customer_group`.

`customer_group` no se utiliza como predictor.

## Parte 1 — Preparación

Ejecuta la instalación de `fairlearn==0.15.0` y recrea el modelo de P01.

Comprueba que `customer_group` no forma parte de `FEATURES`.

## Parte 2 — Contexto de los grupos

Revisa para cada grupo:

- número de solicitudes;
- tasa real de impago;
- riesgo medio predicho.

## Parte 3 — Auditoría con MetricFrame

Para la auditoría se considera resultado favorable:

```text
solvente / aprobado = 1
```

Revisa las métricas globales y desagregadas calculadas por `MetricFrame`:

- accuracy;
- tasa de aprobación;
- recall de clientes solventes;
- precision de aprobación;
- FPR;
- FNR.

## Parte 4 — Criterios de fairness

Compara:

- demographic parity difference;
- demographic parity ratio;
- equal opportunity difference;
- equalized odds difference.

Analiza si todos los criterios conducen a la misma conclusión.

## Parte 5 — Threshold

Modifica únicamente:

```python
THRESHOLD_ELEGIDO
```

Prueba varios valores entre `0.10` y `0.80`.

Observa cómo cambian simultáneamente las métricas por grupo y los criterios de fairness.

## Parte 6 — Interpretación

Analiza:

- si existe un threshold que elimine todas las diferencias;
- qué tipo de error resulta más relevante en este caso;
- por qué excluir `customer_group` del entrenamiento no demuestra fairness;
- qué información adicional sería necesaria antes de emitir una conclusión de auditoría.

## Resultado a conservar

Al terminar la práctica, conserva:

- tabla de métricas por grupo;
- resultados de Fairlearn;
- observaciones sobre el efecto del threshold;
- conclusiones sobre los criterios que producen resultados diferentes.
