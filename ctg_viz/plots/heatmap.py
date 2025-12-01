import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(df: pd.DataFrame) -> None:
    """Heatmap de correlaciones Pearson."""
    num = df.select_dtypes(include="number")
    corr = num.corr()
    plt.figure(figsize=(10,7))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Matriz de correlación")
    plt.show()
