"""
Submódulo de visualizaciones de ctg_viz
"""

from .histograms import plot_histograma
from .boxplots import plot_box
from .barplots import plot_barras
from .density import plot_densidad
from .heatmap import plot_heatmap

__all__ = [
    "plot_histograma",
    "plot_box",
    "plot_barras",
    "plot_densidad",
    "plot_heatmap"
]
