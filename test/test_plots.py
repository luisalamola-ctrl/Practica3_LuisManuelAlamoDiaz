import pandas as pd
from ctg_viz.plots.histograms import plot_histograma
from ctg_viz.plots.boxplots import plot_box
from ctg_viz.plots.barplots import plot_barras
from ctg_viz.plots.density import plot_densidad
from ctg_viz.plots.heatmap import plot_heatmap
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "NSP": [1, 2, 1, 2],
    "LB": [120, 130, 125, 128]
})


def test_plot_histograma():
    plot_histograma(df, "LB", hue="NSP")
    assert plt.gcf() is not None


def test_plot_box():
    plot_box(df, x="NSP", y="LB")
    assert plt.gcf() is not None


def test_plot_barras():
    plot_barras(df, "NSP")
    assert plt.gcf() is not None


def test_plot_densidad():
    plot_densidad(df, col="LB", hue="NSP")
    assert plt.gcf() is not None


def test_plot_heatmap():
    plot_heatmap(df)
    assert plt.gcf() is not None
