# Práctica 3 – Diplomado en Ciencia de Datos

Este repositorio contiene mi entrega de la Práctica 3 del diplomado. Incluye limpieza, imputación, revisión de valores faltantes, detección de outliers y varias visualizaciones aplicadas al dataset CTG.  
También agregué mi librería `ctg_viz`, que armé para tener todas las funciones ordenadas en un paquete reutilizable.

## Contenido del repositorio

- **Practica3LMAD.ipynb / html**  
  Análisis completo de la práctica.

- **ctg_viz/**  
  Librería con funciones para:
  - eliminar nulos
  - imputación (simple y KNN)
  - outliers (IQR y Z-score)
  - reporte de completitud
  - gráficos (histograma, boxplot, barras, densidad y heatmap)

- **requirements.txt**  
  Dependencias necesarias para correr el proyecto.

- **tests/**  
  Pruebas unitarias básicas para validar las funciones de la librería.

## Instalación

Clona el repo:

```bash
git clone https://github.com/luisalamola-ctrl/Practica3_LuisManuelAlamoDiaz.git
