# renombraemails

Este repositorio contiene un script en Python para renombrar archivos de correo electrónico `.eml` y `.msg` usando la fecha de envío.

## Descripción

El script `renombraemails.py` recorre el directorio actual y renombra cada archivo `.eml` o `.msg` que no esté ya renombrado.

Formato de renombrado:

`YYYYMMDD nombre_original.ext`

## Requisitos

- Python 3.8+ (recomendado)
- Dependencias listadas en `requirements.txt`

## Instalación

1. Crear un entorno virtual opcional:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

## Uso

Coloca `renombraemails.py` en la carpeta donde están los archivos `.eml` y `.msg`.

Ejecuta:

```powershell
python renombraemails.py
```

El script:

- procesa archivos `.eml` y `.msg`
- ignora archivos que ya empiezan con `YYYYMMDD`
- renombra cada archivo agregando la fecha de envío al inicio

## Notas

- El script asume que la fecha está presente en la cabecera `Date` de los archivos `.eml`.
- Para archivos `.msg`, usa la librería `extract_msg` para extraer la fecha.

## Licencia

Sin licencia específica.