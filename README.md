# Sistema de Inteligencia Forense Predictiva

Herramienta de análisis y modelado de redes criminales mediante Teoría de Grafos y Redes Neuronales (GNN).

## Descripción
Este sistema implementa un pipeline para la extracción de entidades (Personas, Cuentas, Empresas), la generación de un grafo de conocimiento y el entrenamiento de una Red Convolucional de Grafos (GCN) para la predicción de enlaces ocultos. El objetivo es identificar intermediarios clave y posibles conexiones no registradas en las bases de datos tradicionales.

## Estructura del Proyecto
- `src/ingesta.py`: Generación del grafo heterogéneo, cálculo de métricas de centralidad (Betweenness) y exportación de la matriz de adyacencia.
- `src/modelo_gnn.py`: Implementación de la arquitectura GCN utilizando PyTorch Geometric para el entrenamiento en la predicción de vínculos.

## Tecnologías
- Python 3.11
- PyTorch / PyTorch Geometric
- NetworkX
- Pandas

## Uso
1. Instalar dependencias: `pip install -r requirements.txt`
2. Generar datos y métricas: `python src/ingesta.py`
3. Entrenar el modelo predictivo: `python src/modelo_gnn.py`

## Estado del Proyecto
- [x] Fase 1: Ingesta de datos y modelo base GCN.
- [ ] Fase 2: Implementación de mecanismos de explicabilidad (XAI).
- [ ] Fase 3: Validación con datos de prueba formales.

---
**Investigador:** jusegora
