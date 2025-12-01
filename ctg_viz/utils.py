import pandas as pd

def check_data_completeness_luis_manuel_alamo_diaz(df: pd.DataFrame) -> pd.DataFrame:
    """
    Genera un resumen completo del dataframe:
    - nulos
    - completitud
    - estadísticos numéricos
    - tipo de variable
    
    Returns:
        DataFrame con resumen por columna.
    """
    resumen = []

    uniques = df.nunique(dropna=True)
    cols_num = df.select_dtypes(include="number").columns

    for col in df.columns:
        serie = df[col]
        nulos = serie.isna().sum()
        completitud = 100 - (nulos / len(df) * 100)

        fila = {
            "tipo_dato": str(serie.dtype),
            "nulos": nulos,
            "completitud_%": completitud,
            "n_unicos": uniques[col],
            "tipo_variable": "continua" if col in cols_num and uniques[col] >= 10
                             else "discreta" if col in cols_num
                             else "no_numerica"
        }

        if col in cols_num:
            fila.update({
                "min": serie.min(),
                "max": serie.max(),
                "media": serie.mean(),
                "std": serie.std()
            })
        else:
            fila.update({"min": None, "max": None, "media": None, "std": None})

        resumen.append({"columna": col, **fila})

    return pd.DataFrame(resumen).set_index("columna")
