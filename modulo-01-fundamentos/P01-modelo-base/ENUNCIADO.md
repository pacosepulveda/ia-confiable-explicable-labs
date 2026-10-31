# P01 — Construcción y evaluación del modelo base

## Escenario

Velora Finance está preparando un sistema de apoyo a la evaluación de solicitudes de crédito.

La variable `default` indica si la operación terminó en impago:

- `default = 0`: no hubo impago.
- `default = 1`: hubo impago.

## Archivo principal

- `labs/P01-modelo-base/P01_Velora_Modelo_Base.ipynb`

El notebook contiene el código completo y las explicaciones de cada resultado. No es necesario programar la solución.

## Ejecución

Ejecuta las celdas en orden y revisa las explicaciones que aparecen después de cada resultado.

Durante la práctica se analizarán:

1. distribución de la variable objetivo;
2. separación train/test;
3. entrenamiento del modelo base;
4. probabilidades frente a decisiones binarias;
5. accuracy, precision, recall y F1;
6. matriz de confusión;
7. falsos positivos y falsos negativos;
8. efecto de modificar el threshold;
9. ejemplos concretos de errores del modelo.

ROC-AUC y Precision-Recall aparecen como extensión y pueden utilizarse como demostración del instructor.

## Interacción con el notebook

La única modificación de código propuesta consiste en cambiar:

```python
THRESHOLD_ELEGIDO = 0.30
```

Prueba valores como:

```text
0.20
0.30
0.50
0.60
```

y observa cómo cambian:

- accuracy;
- precision;
- recall;
- F1;
- falsos positivos;
- falsos negativos.

## Preguntas para discutir

- ¿Por qué una accuracy cercana al 90 % puede resultar engañosa?
- ¿Qué significa un falso negativo en este escenario?
- ¿Qué significa un falso positivo?
- ¿Qué ocurre cuando se reduce el threshold?
- ¿Utilizarías el mismo threshold si el principal coste fuera conceder crédito a futuros impagos que si el principal coste fuera rechazar clientes solventes?
- ¿Podemos explicar ya por qué el modelo asigna una probabilidad concreta a una solicitud?

La última pregunta se retomará posteriormente en las prácticas de explicabilidad.
