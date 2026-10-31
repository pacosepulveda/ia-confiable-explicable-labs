# P02 — Auditoría de fairness del modelo de Velora Finance

## Escenario

En P01 se evaluó globalmente el modelo de riesgo de Velora Finance.

En esta práctica se reutiliza el mismo dataset, la misma partición train/test y el mismo modelo para analizar su comportamiento por `customer_group`.

`customer_group` no se utiliza como predictor.

## Parte 1 — Contexto de los grupos

Ejecuta las celdas iniciales y revisa para cada grupo:

- número de solicitudes;
- tasa real de impago;
- probabilidad media de impago estimada.

## Parte 2 — Métricas desagregadas

Con `threshold = 0.50`, compara:

- tasa de alto riesgo;
- tasa de aprobación;
- accuracy;
- precision;
- detección de impagos;
- FPR;
- FNR;
- aprobación de clientes realmente solventes;
- aprobación de operaciones que realmente terminan en impago.

Identifica qué métricas presentan las mayores diferencias.

## Parte 3 — Criterios de fairness

Revisa los diagnósticos calculados para:

- demographic parity;
- equal opportunity;
- equalized odds;
- diferencia en detección de impagos.

Compara las conclusiones que produciría cada criterio.

## Parte 4 — Threshold

Modifica únicamente el control:

```python
THRESHOLD_ELEGIDO
```

Prueba varios valores entre `0.10` y `0.80`.

Comprueba cómo cambian simultáneamente:

- rendimiento;
- tasas de aprobación;
- FPR y FNR;
- diferencias entre grupos.

## Parte 5 — Atributo de auditoría

Comprueba que `customer_group` no forma parte de `FEATURES`.

Analiza si la exclusión del atributo es suficiente para garantizar que no existan diferencias de comportamiento.

## Parte 6 — Calibración

Revisa la tabla y el gráfico de calibración por grupo.

Compara:

- riesgo medio predicho;
- tasa de impago observada.

## Resultado a conservar

Al terminar la práctica, conserva:

- tabla de métricas por grupo;
- diagnósticos de fairness;
- observaciones sobre el efecto del threshold;
- gráfico de calibración.
