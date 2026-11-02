# Recursos compartidos

Esta carpeta contiene utilidades utilizadas por varias prácticas del curso.

## `generate_velora_credit.py`

Genera de forma reproducible el dataset sintético de **Velora Finance** utilizado durante el curso.

Para generar el archivo de datos desde la raíz del repositorio:

```bash
python resources/generate_velora_credit.py
```

El script utiliza una semilla fija y genera `data/velora_credit.csv.gz`. También expone la función `generate_dataset()`, que puede importarse directamente desde los notebooks.

Consulta [`data/README.md`](../data/) para ver la descripción de los campos del dataset.
