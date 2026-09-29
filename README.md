# Análisis de Producción de Café en Fincas

Proyecto de análisis de datos con **Pandas** sobre un dataset de fincas cafeteras (`fincas_produccion_cafe.csv`). Incluye selección y filtrado de datos, limpieza, imputación de nulos, creación de columnas y agrupaciones con `.agg()`.

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `AnalisisDatos.ipynb` | Notebook de Jupyter con el análisis paso a paso |
| `analisis_fincas_cafe.py` | Versión en script de Python del análisis |
| `fincas_produccion_cafe.csv` | Dataset con los datos de las fincas |
| `requirements.txt` | Librerías necesarias para ejecutar el proyecto |
| `.gitignore` | Archivos y carpetas excluidos del repositorio (`.vscode/`, `venv/`, `datos/`) |

## Requisitos previos

- [Python 3.14.7](https://www.python.org/downloads/) (durante la instalación en Windows, marca la casilla **Add Python to PATH**)
- [Git](https://git-scm.com/downloads)
- [Visual Studio Code](https://code.visualstudio.com/) con las extensiones **Python** y **Jupyter**

Para comprobar que Python y Git están instalados:

```bash
python --version
git --version
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/JohnDeivid12/Analisis-Dataset-Produccion-de-Cafe-Fincas-Caldenses.git
(datos) 
```

> Reemplaza `TU_USUARIO` y `NOMBRE_DEL_REPOSITORIO` por los datos de tu repositorio.

### 2. Crear un entorno virtual

El entorno virtual (`venv/`) aísla las librerías del proyecto. No se sube a GitHub porque está en el `.gitignore`, así que cada persona debe crearlo en su equipo.

**Windows (PowerShell o CMD):**

```bash
python -m venv datos
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv datos
source venv/bin/activate
```

Cuando el entorno está activo, verás `(venv)` al inicio de la línea de la terminal.

> Si PowerShell bloquea la activación, ejecuta una vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

### 3. Instalar las dependencias

Si `requirements.txt` no incluye las herramientas de Jupyter, instálalas también:

```bash
pip install jupyter ipykernel
```

## Ejecución

### Opción A: Notebook en Visual Studio Code

1. Abre la carpeta del proyecto en VS Code (`File > Open Folder`).
2. Abre el archivo `AnalisisDatos.ipynb`.
3. Arriba a la derecha, haz clic en **Select Kernel** , Entorno de Python, Crear entorno de Python, Introducir Ruta del Interprete, seleccionas la carpeta datos y el kernel mostrara algo asi: (`datos (3.14.7) (Python 3.14.7`).
4. Ejecuta las celdas en orden con **Run All** o con `Shift + Enter` en cada una.

### Opción B: Notebook en el navegador

```bash
jupyter notebook
```

Se abrirá el navegador; selecciona `AnalisisDatos.ipynb`.

### Opción C: Script de Python

```bash
python analisis_fincas_cafe.py
```

## Notas importantes

- **Ruta del CSV:** el archivo `fincas_produccion_cafe.csv` debe estar en la misma carpeta que el notebook y el script, ya que se lee con `pd.read_csv("fincas_produccion_cafe.csv")`.
- **Orden de ejecución:** ejecuta las celdas del notebook de arriba hacia abajo. A partir del paso de renombrado, las columnas `Metodo_Beneficio` y `Altitud_MSNM` pasan a llamarse `Beneficio` y `Altitud`.
- **Carpeta `datos/`:** está en el `.gitignore`, por lo que cualquier archivo que guardes allí no se sube al repositorio.

## Solución de problemas

| Problema | Solución |
|---|---|
| `ModuleNotFoundError: No module named 'pandas'` | El entorno virtual no está activo o faltó instalar las dependencias. Activa `venv` y ejecuta `pip install -r requirements.txt`. |
| No aparece el kernel de `venv` en VS Code | Ejecuta `pip install ipykernel` y reinicia VS Code. |
| `FileNotFoundError` al leer el CSV | Abre VS Code en la carpeta del proyecto, no en una carpeta superior. |
| `KeyError` al usar `.loc[280]` | Ese índice no existe en el dataset. Comprueba el máximo con `df.index.max()`. |

## Tecnologías

- Python
- Pandas
- Jupyter Notebook
