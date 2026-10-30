# Datos de Aurea Finance

El fichero de trabajo se genera con:

```bash
python resources/generate_aurea_credit.py
```

El resultado es:

```text
data/aurea_credit.csv.gz
```

Puede cargarse directamente con pandas:

```python
import pandas as pd

df = pd.read_csv("data/aurea_credit.csv.gz")
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

La versión actual genera 3.000 solicitudes con semilla fija `42`.

La tasa global de `default` está alrededor del 12%, con diferencias entre los grupos A y B. `customer_group` no se utiliza como predictor en P01.
