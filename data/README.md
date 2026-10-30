# Datos de Velora Finance

El repositorio incluye:

```text
data/velora_credit.csv.gz
```

Puede cargarse directamente con pandas:

```python
import pandas as pd

df = pd.read_csv("data/velora_credit.csv.gz")
```

También puede regenerarse de forma reproducible desde la raíz del repositorio:

```bash
python resources/generate_velora_credit.py
```

## Campos

| Campo | Descripción |
|---|---|
| `application_id` | Identificador de la solicitud |
| `age` | Edad del solicitante |
| `annual_income` | Ingresos anuales |
| `debt_ratio` | Ratio de endeudamiento |
| `employment_months` | Antigüedad laboral en meses |
| `late_payments_12m` | Número de pagos tardíos en los últimos 12 meses |
| `credit_history_months` | Antigüedad del historial crediticio en meses |
| `existing_debt` | Deuda existente |
| `requested_amount` | Importe solicitado |
| `savings_balance` | Saldo de ahorro disponible |
| `customer_group` | Grupo sintético utilizado en análisis posteriores |
| `default` | Variable objetivo: `1` = impago, `0` = no impago |

## Tamaño y distribución

La versión actual contiene 3.000 solicitudes generadas con semilla fija `42`.

La tasa global de `default` es aproximadamente del 11,6%. `customer_group` no se utiliza como predictor en P01.
