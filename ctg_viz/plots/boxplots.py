import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_box(df: pd.DataFrame, x: str, y: str) -> None:
    """Boxplot simple."""
    plt.figure(figsize=(7,5))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f"Boxplot de {y} por {x}")
    plt.show()
