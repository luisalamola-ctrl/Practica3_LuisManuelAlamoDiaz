import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograma(df: pd.DataFrame, columna: str, hue: str = None) -> None:
    """Histograma con KDE."""
    plt.figure(figsize=(8,5))
    sns.histplot(df, x=columna, hue=hue, kde=True, stat="density", bins=30)
    plt.title(f"Histograma de {columna}")
    plt.show()
