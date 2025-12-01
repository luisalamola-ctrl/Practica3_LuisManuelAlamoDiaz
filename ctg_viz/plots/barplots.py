import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_barras(df: pd.DataFrame, col: str) -> None:
    """Barplot de frecuencias."""
    conteos = df[col].value_counts()
    plt.figure(figsize=(7,5))
    sns.barplot(x=conteos.values, y=conteos.index)
    plt.title(f"Frecuencias de {col}")
    plt.show()
