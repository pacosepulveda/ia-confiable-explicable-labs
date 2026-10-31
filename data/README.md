# Datos de Velora Finance

El dataset utilizado en P01 se genera de forma reproducible mediante:

```bash
python resources/generate_velora_credit.py
```

El notebook `labs/P01-modelo-base/P01_Velora_Modelo_Base.ipynb` utiliza directamente la función `generate_dataset()` de ese script.

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

La versión actual genera 3.000 solicitudes con semilla fija `42`. La tasa global de `default` es aproximadamente del 11,6%. `customer_group` no se utiliza como predictor en P01.
