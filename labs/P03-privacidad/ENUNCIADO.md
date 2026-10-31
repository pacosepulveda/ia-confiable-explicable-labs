# P03 — Privacidad, utilidad y aprendizaje distribuido

## Escenario

Velora Finance quiere obtener estadísticas y entrenar modelos utilizando datos distribuidos, limitando la exposición de información individual.

La práctica utiliza el mismo dataset sintético del caso Velora Finance.

## Parte 1 — Consulta agregada

Trabaja con el cohorte de auditoría de 600 solicitudes y calcula su tasa exacta de impago.

## Parte 2 — Differential Privacy

Ejecuta el mecanismo de Laplace preparado en el notebook.

Modifica:

```python
EPSILON
```

Observa:

- tasa exacta;
- tasa publicada con DP;
- ruido añadido;
- error absoluto.

## Parte 3 — Privacidad y utilidad

Ejecuta la simulación repetida para distintos valores de `epsilon`.

Compara:

- error absoluto medio;
- percentil 95 del error.

Analiza el trade-off entre privacidad y utilidad.

## Parte 4 — Tamaño de grupo

Modifica:

```python
EPSILON_GRUPOS
```

Compara el efecto del mismo mecanismo sobre los diferentes grupos de auditoría.

## Parte 5 — Composición

Modifica:

```python
EPSILON_POR_CONSULTA
NUM_CONSULTAS
```

Observa cómo cambia la cota básica del presupuesto acumulado.

## Parte 6 — Federated Learning

Ejecuta la simulación simplificada de entrenamiento distribuido.

Revisa:

- número de silos;
- número de parámetros intercambiados;
- filas brutas enviadas al agregador;
- ROC-AUC obtenida.

Identifica qué riesgos de privacidad permanecen aunque los datos brutos no se centralicen.

## Resultado a conservar

Al terminar la práctica, conserva:

- tabla privacidad/utilidad;
- resultados por grupo;
- presupuesto acumulado utilizado en el ejemplo;
- conclusiones sobre las diferencias entre Differential Privacy y Federated Learning.
