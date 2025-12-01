import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_densidad(df: pd.DataFrame, col: str, hue: str) -> None:
    """Densidad por clase."""
    plt.figure(figsize=(8,5))
    sns.kdeplot(data=df, x=col, hue=hue, fill=True, alpha=0.4)
    plt.title(f"Densidad de {col}")
    plt.show()
