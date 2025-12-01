import pandas as pd
import numpy as np
from ctg_viz.preprocessing import (
    eliminar_nulos_altos,
    imputar_valores,
    imputar_knn,
    eliminar_outliers_iqr,
    eliminar_outliers_zscore
)


def test_eliminar_nulos_altos():
    df = pd.DataFrame({
        "a": [1, None, None],   # 66% nulos → debe eliminarse
        "b": [1, 2, 3]          # 0% nulos → se conserva
    })

    df2 = eliminar_nulos_altos(df, umbral=0.5)
    assert "a" not in df2.columns
    assert "b" in df2.columns



def test_imputar_knn():
    df = pd.DataFrame({
        "a": [1, 2, None],
        "b": [2, None, 6]
    })

    df2 = imputar_knn(df, vecinos=2)

    assert df2.isna().sum().sum() == 0   # KNN debe imputar todo


def test_eliminar_outliers_iqr():
    df = pd.DataFrame({
        "v": [10, 12, 11, 13, 999]  # 999 es outlier gigante
    })

    df2 = eliminar_outliers_iqr(df)

    assert len(df2) == 4
    assert 999 not in df2["v"].values
