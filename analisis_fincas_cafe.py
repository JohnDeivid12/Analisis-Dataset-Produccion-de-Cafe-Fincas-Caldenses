"""
Analisis de datos de fincas productoras de cafe (Eje 1: Pandas basico)
Dataset: fincas_produccion_cafe.csv  ->  1012 observaciones, 8 variables
"""

import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 160)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

RUTA_CSV = "fincas_produccion_cafe.csv"


def encabezado(titulo):
    print("\n" + "=" * 78)
    print(titulo)
    print("=" * 78)


# ---------------------------------------------------------------------------
# 1. Lectura y verificacion estructural
# ---------------------------------------------------------------------------
encabezado("1. LECTURA Y VERIFICACION ESTRUCTURAL")

# index_col NO se usa a proposito: el indice queda como RangeIndex (0..n-1),
# que es lo que permite consultar por posicion con .loc[] mas adelante
# (indice 280) y evita tener una columna de indice numerico adicional
# (tipo "Unnamed: 0") que duplique la numeracion de filas.
df_fincas = pd.read_csv(RUTA_CSV, encoding="utf-8")

print("Tipo de objeto      :", type(df_fincas).__name__)
print("Dimensiones         :", df_fincas.shape)
print("Columnas duplicadas :", [c for c in df_fincas.columns if str(c).startswith("Unnamed")] or "ninguna")
print("Tipo de indice      :", type(df_fincas.index).__name__)
print("\nColumnas y tipos de dato:")
print(df_fincas.dtypes.to_string())
print("\nPrimeras 5 filas:")
print(df_fincas.head().to_string(index=False))

# ---------------------------------------------------------------------------
# 2. Seleccion unidimensional y proyeccion multivariable
# ---------------------------------------------------------------------------
encabezado("2. SELECCION UNIDIMENSIONAL Y PROYECCION MULTIVARIABLE")

# Una sola columna -> Serie de pandas
serie_variedades = df_fincas["Variedad"]
print("Tipo de la seleccion unidimensional:", type(serie_variedades).__name__)
print("Valores unicos de Variedad (", serie_variedades.nunique(), "):")
print(sorted(serie_variedades.unique().tolist()))
print("Conteo por variedad:")
print(serie_variedades.value_counts().to_string())

# Varias columnas -> vista de tabla (DataFrame)
vista_produccion = df_fincas[["Municipio", "Area_Hectareas", "Kilos_Recolectados"]]
print("\nTipo de la proyeccion multivariable:", type(vista_produccion).__name__, "->", vista_produccion.shape)
print(vista_produccion.head().to_string(index=False))

# ---------------------------------------------------------------------------
# 3. Acceso por etiqueta con .loc[]
# ---------------------------------------------------------------------------
encabezado("3. ACCESO POR ETIQUETA (.loc) - PREDIO EN LA POSICION 280")

predio_280 = df_fincas.loc[280]
print("Tipo del resultado:", type(predio_280).__name__)
print(predio_280.to_string())

# ---------------------------------------------------------------------------
# 4. Eliminacion de filas duplicadas
# ---------------------------------------------------------------------------
encabezado("4. ELIMINACION DE FILAS DUPLICADAS")

filas_antes = len(df_fincas)
duplicados = int(df_fincas.duplicated().sum())

df_fincas = df_fincas.drop_duplicates().reset_index(drop=True)

print(f"Filas antes de limpiar : {filas_antes}")
print(f"Observaciones repetidas eliminadas: {duplicados}")
print(f"Filas despues de limpiar        : {len(df_fincas)}")
print("Duplicados restantes    :", int(df_fincas.duplicated().sum()))

# ---------------------------------------------------------------------------
# 5. Filtrado condicional basico (boolean mask)
# ---------------------------------------------------------------------------
encabezado("5. FILTRADO CONDICIONAL BASICO - Altitud_MSNM > 1750")

filtro_altura = df_fincas[df_fincas["Altitud_MSNM"] > 1750]
print("Lotes a gran altura (> 1750 msnm):", len(filtro_altura))
print(filtro_altura.head(10).to_string(index=False))

# ---------------------------------------------------------------------------
# 6. Filtrado categorico por lista (.isin)
# ---------------------------------------------------------------------------
encabezado("6. FILTRADO CATEGORICO POR LISTA (.isin) - Anserma y Risaralda")

filtro_municipios = df_fincas[df_fincas["Municipio"].isin(["Anserma", "Risaralda"])]
print("Lotes en Anserma o Risaralda:", len(filtro_municipios))
print(filtro_municipios["Municipio"].value_counts().to_string())

# ---------------------------------------------------------------------------
# 7. Filtrado por intervalo numerico (.between)
# ---------------------------------------------------------------------------
encabezado("7. FILTRADO POR INTERVALO NUMERICO (.between) - 3.0 a 8.0 ha")

filtro_area = df_fincas[df_fincas["Area_Hectareas"].between(3.0, 8.0)]
print("Lotes con area entre 3.0 y 8.0 ha (inclusive):", len(filtro_area))
print("Areas presentes en el subconjunto:", sorted(filtro_area["Area_Hectareas"].unique().tolist()))

# ---------------------------------------------------------------------------
# 8. Consultas directas con .query()
# ---------------------------------------------------------------------------
encabezado("8. CONSULTAS DIRECTAS CON .query()")

organicos_voluminosos = df_fincas.query("Certificacion == 'Orgánico' and Kilos_Recolectados > 5000")
print("Fincas organicas con mas de 5000 kg:", len(organicos_voluminosos))
print(organicos_voluminosos.head(10).to_string(index=False))

# ---------------------------------------------------------------------------
# 9. Filtrado compuesto con metodos de texto (&)
# ---------------------------------------------------------------------------
encabezado("9. FILTRADO COMPUESTO CON METODOS DE TEXTO (.str.startswith + &)")

condicion_lavado_geisha = (
    df_fincas["Metodo_Beneficio"].str.startswith("Lavado")
    & (df_fincas["Variedad"] == "Geisha")
)
filtro_lavado_geisha = df_fincas[condicion_lavado_geisha]
print("Fincas con beneficio 'Lavado...' y variedad Geisha:", len(filtro_lavado_geisha))
print(filtro_lavado_geisha.head(10).to_string(index=False))

# ---------------------------------------------------------------------------
# 10. Imputacion de valores faltantes
# ---------------------------------------------------------------------------
encabezado("10. IMPUTACION DE VALORES FALTANTES (.fillna)")

faltantes_antes = df_fincas[["Area_Hectareas", "Kilos_Recolectados"]].isna().sum()
print("NaN antes de imputar:")
print(faltantes_antes.to_string())

promedio_area = df_fincas["Area_Hectareas"].mean()
print(f"\nPromedio general de Area_Hectareas (ignora NaN): {promedio_area:,.4f} ha")

df_fincas["Area_Hectareas"] = df_fincas["Area_Hectareas"].fillna(promedio_area)
df_fincas["Kilos_Recolectados"] = df_fincas["Kilos_Recolectados"].fillna(0.0)

print("\nNaN despues de imputar:")
print(df_fincas[["Area_Hectareas", "Kilos_Recolectados"]].isna().sum().to_string())

# ---------------------------------------------------------------------------
# 11. Transformacion y creacion de columnas con .apply()
# ---------------------------------------------------------------------------
encabezado("11. TRANSFORMACION Y CREACION DE COLUMNAS (.apply)")


def calcular_rendimiento(fila):
    """Rendimiento en kilos por hectarea: Kilos_Recolectados / Area_Hectareas."""
    area = fila["Area_Hectareas"]
    if pd.isna(area) or area == 0:
        return float("nan")
    return fila["Kilos_Recolectados"] / area


df_fincas["Rendimiento_Kilos_Ha"] = df_fincas.apply(calcular_rendimiento, axis=1)

print("Columna creada: Rendimiento_Kilos_Ha")
print(df_fincas[["ID_Finca", "Area_Hectareas", "Kilos_Recolectados", "Rendimiento_Kilos_Ha"]].head(10).to_string(index=False))
print("\nEstadisticas del rendimiento (kg/ha):")
print(df_fincas["Rendimiento_Kilos_Ha"].describe().to_string())

# ---------------------------------------------------------------------------
# 12. Renombrado y reordenamiento de atributos
# ---------------------------------------------------------------------------
encabezado("12. RENOMBRADO (.rename) Y REORDENAMIENTO DE ATRIBUTOS")

df_fincas = df_fincas.rename(
    columns={"Metodo_Beneficio": "Beneficio", "Altitud_MSNM": "Altitud"}
)

primeras = ["ID_Finca", "Rendimiento_Kilos_Ha"]
resto = [c for c in df_fincas.columns if c not in primeras]
df_fincas = df_fincas[primeras + resto]

print("Columnas resultantes (en orden):")
for i, c in enumerate(df_fincas.columns, start=1):
    print(f"  {i:>2}. {c}")
print("\nVista final:")
print(df_fincas.head(10).to_string(index=False))

# ---------------------------------------------------------------------------
# 13. Agrupacion y metricas de produccion por Municipio
# ---------------------------------------------------------------------------
encabezado("13. AGRUPACION POR MUNICIPIO (.agg): promedio de Altitud y suma de Kilos")

metricas_municipio = df_fincas.groupby("Municipio", as_index=False).agg(
    Altitud_Promedio=("Altitud", "mean"),
    Kilos_Total=("Kilos_Recolectados", "sum"),
)
print(metricas_municipio.to_string(index=False))
print("\nTotal de kilos del municipio mas productivo:",
      metricas_municipio.loc[metricas_municipio["Kilos_Total"].idxmax(), "Municipio"],
      f"({metricas_municipio['Kilos_Total'].max():,.0f} kg)")

# ---------------------------------------------------------------------------
# 14. Dispersion con funcion personalizada (.agg + rango)
# ---------------------------------------------------------------------------
encabezado("14. DISPERSION CON FUNCION PERSONALIZADA (.agg + rango)")


def rango(serie):
    """Rango = valor maximo - valor minimo."""
    return serie.max() - serie.min()


dispersion_variedad = df_fincas.groupby("Variedad", as_index=False).agg(
    Rango_Area_Hectareas=("Area_Hectareas", rango),
    Rango_Kilos_Recolectados=("Kilos_Recolectados", rango),
)
print(dispersion_variedad.to_string(index=False))

# ---------------------------------------------------------------------------
# 15. Agrupamiento multinivel (Municipio + Variedad)
# ---------------------------------------------------------------------------
encabezado("15. AGRUPAMIENTO MULTINIVEL (Municipio + Variedad)")

metricas_multinivel = df_fincas.groupby(
    ["Municipio", "Variedad"], as_index=False
).agg(
    Altitud_Promedio=("Altitud", "mean"),
    Kilos_Total=("Kilos_Recolectados", "sum"),
)

print("Combinaciones Municipio/Variedad:", len(metricas_multinivel))
print(metricas_multinivel.head(20).to_string(index=False))
print("\nLas 10 combinaciones con mayor produccion:")
print(
    metricas_multinivel.sort_values("Kilos_Total", ascending=False)
    .head(10)
    .to_string(index=False)
)

# ---------------------------------------------------------------------------
encabezado("RESUMEN DEL DATAFRAME FINAL")
print(df_fincas.info())
print("\nValores faltantes restantes:", int(df_fincas.isna().sum().sum()))
