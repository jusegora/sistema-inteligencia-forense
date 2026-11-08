# Analisis Forense de Redes

Scripts desarrollados para analizar estructuras criminales usando teoria de grafos y redes neuronales.

## Componentes
- `src/ingesta.py`: Genera los datos sinteticos y calcula centralidad (NetworkX).
- `src/modelo_gnn.py`: Entrena un modelo GCN (PyTorch Geometric) para predecir enlaces.
- `src/visualizacion.py`: Exporta un grafo visual con Matplotlib.
- `src/reporte_forense.py`: Genera un informe de texto con los hallazgos.

## Uso
Ejecutar en orden: `ingesta.py`, `modelo_gnn.py`, `visualizacion.py`, `reporte_forense.py`.
