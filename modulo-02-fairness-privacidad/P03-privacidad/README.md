# P03 — Differential Privacy con PyTorch y Opacus

Laboratorio basado en el caso **Velora Finance**.

## 🚀 Abrir en Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pacosepulveda/ia-confiable-explicable-labs/blob/main/modulo-02-fairness-privacidad/P03-privacidad/P03_Velora_Privacidad.ipynb)

📋 [Leer el enunciado](./ENUNCIADO.md)

Al abrir el notebook en Colab, usa **Archivo → Guardar una copia en Drive** para conservar tus cambios.

## Aceleración recomendada

Activa **Entorno de ejecución → Cambiar tipo de entorno de ejecución → GPU T4** antes de ejecutar el entrenamiento PyTorch/Opacus.

## Contenido

- PyTorch;
- Opacus 1.6.0;
- DP-SGD;
- clipping por ejemplo;
- ruido calibrado;
- `noise_multiplier`;
- `max_grad_norm`;
- sampling y epochs;
- presupuesto `(epsilon, delta)`;
- contabilidad de epsilon por epoch;
- comparación entre entrenamiento convencional y privado;
- trade-off privacidad / utilidad;
- comparación de utilidad por `customer_group`;
- composición básica del presupuesto durante reentrenamientos;
- relación entre Differential Privacy y Federated Learning;
- limitaciones de Federated Learning como mecanismo de privacidad.

## Estado

✅ Notebook validado en Google Colab con GPU T4.
