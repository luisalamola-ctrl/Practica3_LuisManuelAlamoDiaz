import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer


"""
Funciones de preprocesamiento 

Incluye:
- Eliminación de columnas con nulos altos
- Imputación por media / moda
- Imputación KNN
- Outliers por IQR
- Outliers por Z-score
"""


def eliminar_nulos_altos(df: pd.DataFrame, umbral: float = 0.20) -> pd.DataFrame:
    """
    Elimina columnas cuyo porcentaje de valores nulos supera el umbral.
    """
    mask = df.isna().mean() < umbral
    return df.loc[:, mask]


def imputar_valores(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    Regla:
    - Si es numérica y tiene >= 10 valores únicos → imputar MEDIA
    - Si es numérica y tiene < 10 valores unicos  → imputar MODA
    - Si NO es numérica                           → imputar MODA
    """
    df_imp = df.copy()

    # conteo de valores únicos por columna
    n_unique = df_imp.nunique()

    # detectar numéricas y categóricas
    cols_num = df_imp.select_dtypes(include="number").columns
    cols_no_num = df_imp.columns.difference(cols_num)

    continuas = [c for c in cols_num if n_unique[c] >= 10]
    discretas = [c for c in cols_num if n_unique[c] < 10]

    for col in continuas:
        df_imp[col] = df_imp[col].fillna(df_imp[col].mean())


    for col in discretas:
        moda = df_imp[col].mode(dropna=True)
        if not moda.empty:
            df_imp[col] = df_imp[col].fillna(moda.iloc[0])

    for col in cols_no_num:
        moda = df_imp[col].mode(dropna=True)
        if not moda.empty:
            df_imp[col] = df_imp[col].fillna(moda.iloc[0])

    return df_imp


def imputar_knn(df: pd.DataFrame, vecinos: int = 5) -> pd.DataFrame:
    """
    Imputación KNN para columnas numéricas.
    """
    df_copy = df.copy()
    cols_num = df_copy.select_dtypes(include="number").columns

    imputer = KNNImputer(n_neighbors=vecinos)
    df_copy[cols_num] = imputer.fit_transform(df_copy[cols_num])

    return df_copy


def eliminar_outliers_iqr(df: pd.DataFrame, factor: float = 1.5) -> pd.DataFrame:
    """
    Elimina outliers usando el método IQR (FACTOR DEFAULT=1.5)
    """
    df_proc = df.copy()
    cols = df_proc.select_dtypes(include="number").columns

    mask_eliminar = np.zeros(len(df_proc), dtype=bool)

    for col in cols:
        serie = df_proc[col].dropna()

        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)
        iqr = q3 - q1

        lim_inf = q1 - factor * iqr
        lim_sup = q3 + factor * iqr

        mask = (df_proc[col] < lim_inf) | (df_proc[col] > lim_sup)
        mask_eliminar |= mask

    return df_proc.loc[~mask_eliminar].reset_index(drop=True)


def eliminar_outliers_zscore(df: pd.DataFrame, umbral: float = 3) -> pd.DataFrame:
    """
    Elimina outliers usando Z-score columna por columna.
    """
    df_copy = df.copy()
    cols = df_copy.select_dtypes(include="number").columns

    mask = np.zeros(len(df_copy), dtype=bool)

    for col in cols:
        serie = df_copy[col]

        z = (serie - serie.mean()) / serie.std(ddof=0)

        mask |= (np.abs(z) > umbral)

    return df_copy.loc[~mask].reset_index(drop=True)
