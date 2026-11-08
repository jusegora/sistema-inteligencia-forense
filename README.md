# Sistema de Inteligencia Forense Predictiva y Explicable

**Investigador:** jusegora  
*Abogado Especialista en Derecho Procesal Penal y Criminalística*

Herramienta avanzada para el análisis, modelado y generación de informes periciales sobre redes criminales, utilizando Teoría de Grafos y Redes Neuronales (GNN).

## Arquitectura del Proyecto
Este sistema fue diseñado para superar las limitaciones de los softwares de análisis de enlaces tradicionales (estáticos y secuenciales), implementando un enfoque de inteligencia predictiva.

- **`src/ingesta.py`**: Genera un Grafo de Conocimiento Heterogéneo (Personas, Cuentas, Empresas) y calcula métricas topológicas como la centralidad de intermediación (Betweenness).
- **`src/modelo_gnn.py`**: Implementación de una Red Convolucional de Grafos (GCN) mediante PyTorch Geometric para la predicción de enlaces ocultos no registrados en las bases de datos.
- **`src/visualizacion.py`**: Motor de renderizado que genera grafos visuales ponderados por riesgo, facilitando la interpretación de estructuras criminales complejas.
- **`src/reporte_forense.py`**: Módulo de automatización que consolida los hallazgos matemáticos en un informe técnico pericial, listo para ser presentado ante autoridades judiciales.

## Tecnologías
- Python 3.11
- PyTorch / PyTorch Geometric (GNNs)
- NetworkX (Graph Analytics)
- Matplotlib

## Uso
1. Generar la red y métricas: `python src/ingesta.py`
2. Entrenar el modelo GCN: `python src/modelo_gnn.py`
3. Visualizar el grafo: `python src/visualizacion.py`
4. Generar el informe pericial: `python src/reporte_forense.py`

---
*Nota: Los datos utilizados en este repositorio son sintéticos y han sido generados con fines de validación metodológica.*
