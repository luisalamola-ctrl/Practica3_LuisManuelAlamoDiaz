import pandas as pd
from ctg_viz.utils import check_data_completeness_luis_manuel_alamo_diaz


def check_data_completeness_luis_manuel_alamo_diaz():
    df = pd.DataFrame({
        "x": [1, 2, None],
        "y": ["a", None, "b"]
    })

    res = check_data_completitud(df)

    # Debe devolver un DataFrame con índice = columnas
    assert "x" in res.index
    assert "y" in res.index

    # Completitud de x = 2/3 = 66.66%
    assert round(res.loc["x", "completitud_%"], 2) == round(66.666666, 2)

    # Tipo numérico para x
    assert res.loc["x", "tipo_variable"] in ["continua", "discreta"]

    # y no es numérica
    assert res.loc["y", "tipo_variable"] == "no_numerica"
