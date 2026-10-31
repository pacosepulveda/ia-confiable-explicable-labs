# P02 — Auditoría y mitigación de fairness con Fairlearn

## Escenario

En P01 se evaluó globalmente el modelo de riesgo de Velora Finance.

En esta práctica se reutiliza el mismo caso para analizar su comportamiento por `customer_group` y probar una mitigación real mediante postprocesado.

`customer_group` no se utiliza como predictor del modelo base.

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

Compara además:

- demographic parity difference;
- demographic parity ratio;
- equal opportunity difference;
- equalized odds difference.

## Parte 4 — Threshold

Modifica únicamente:

```python
THRESHOLD_ELEGIDO
```

Prueba varios valores entre `0.10` y `0.80`.

Observa cómo cambian simultáneamente las métricas por grupo y los criterios de fairness.

## Parte 5 — Calibración por grupo

Revisa la tabla y el gráfico de calibración.

Compara, para cada grupo e intervalo de score:

- riesgo medio predicho;
- impago observado.

Analiza si una probabilidad similar conserva un significado comparable entre grupos.

## Parte 6 — Separación de datos para mitigación

La segunda mitad del notebook utiliza tres conjuntos independientes:

1. entrenamiento del modelo base;
2. calibración del postprocesado;
3. test final.

Comprueba que el test final no se utiliza para seleccionar la política de mitigación.

## Parte 7 — Mitigación con ThresholdOptimizer

Ejecuta `ThresholdOptimizer` con:

```text
constraints = equalized_odds
objective   = accuracy_score
```

El postprocesador no reentrena la regresión logística. Aprende una política de decisión posterior utilizando los scores del modelo y `customer_group` como `sensitive_features`.

## Parte 8 — Comparación Base vs Mitigado

Sobre el mismo test final, compara:

- accuracy;
- tasa de aprobación;
- recall de solventes;
- FPR;
- FNR;
- demographic parity difference;
- equal opportunity difference;
- equalized odds difference.

Analiza:

- qué disparidad se reduce;
- qué coste de rendimiento aparece;
- qué errores se redistribuyen;
- qué implica usar thresholds distintos por grupo;
- qué documentación y aprobación requeriría la intervención.

## Resultado a conservar

Al terminar la práctica, conserva:

- tabla de métricas por grupo;
- métricas de fairness;
- observaciones sobre el efecto del threshold;
- tabla/gráfico de calibración;
- comparación Base vs Mitigado;
- conclusión razonada sobre si aceptarías o no la política mitigada.
