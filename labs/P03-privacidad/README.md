# P03 — Differential Privacy con PyTorch y Opacus

Laboratorio basado en el caso **Velora Finance**.

## Archivos

- `ENUNCIADO.md`
- `P03_Velora_Privacidad.ipynb`
- `../../resources/generate_velora_credit.py`

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

## Aceleración

La práctica utiliza GPU T4 en Google Colab cuando está disponible para el entrenamiento PyTorch/Opacus.

## Estado

✅ Notebook validado en Google Colab con GPU T4.
