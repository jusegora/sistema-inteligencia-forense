import json
import networkx as nx
import os

def generar_informe():
    print("Cargando datos para el informe...")
    with open('data/grafo_forense.json', 'r') as f:
        datos = json.load(f)

    G = nx.DiGraph()
    for n in datos["nodos"]:
        G.add_node(n["id"], tipo=n["tipo"])
    for e in datos["aristas"]:
        G.add_edge(e["source"], e["target"])

    # Calculo de metricas
    centralidad = nx.betweenness_centrality(G)
    grados = dict(G.degree())
    
    # Ordenar por centralidad
    nodos_criticos = sorted(centralidad.items(), key=lambda x: x[1], reverse=True)[:5]
    
    lineas_informe = []
    lineas_informe.append("==================================================")
    lineas_informe.append("INFORME TECNICO DE ANALISIS DE REDES CRIMINALES")
    lineas_informe.append("==================================================")
    lineas_informe.append(f"Total de entidades analizadas: {len(datos['nodos'])}")
    lineas_informe.append(f"Total de relaciones identificadas: {len(datos['aristas'])}")
    lineas_informe.append("--------------------------------------------------")
    lineas_informe.append("1. IDENTIFICACION DE NODOS CRITICOS (INTERMEDIARIOS)")
    lineas_informe.append("Los siguientes nodos presentan los indices mas altos de intermediacion, indicando un rol de control o paso obligado en la red:")
    
    for i, (nodo, score) in enumerate(nodos_criticos, 1):
        tipo = G.nodes[nodo]['tipo']
        lineas_informe.append(f"   [{i}]. Entidad: {nodo} | Tipo: {tipo} | Indice de Intermediacion: {score:.4f}")

    lineas_informe.append("--------------------------------------------------")
    lineas_informe.append("2. CONCLUSIONES PRELIMINARES")
    
    top_nodo = nodos_criticos[0][0]
    lineas_informe.append(f"El nodo '{top_nodo}' actua como el principal eje articulador de la red. La interrupcion de sus vinculos o el rastreo de sus transacciones representa la linea de investigacion con mayor probabilidad de exito para desarticular la estructura.")
    
    lineas_informe.append("==================================================")
    lineas_informe.append("Fin del informe. Documento generado para uso de inteligencia.")

    # Escribir el archivo
    os.makedirs('data', exist_ok=True)
    with open('data/informe_pericial.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lineas_informe))
        
    print("Informe generado correctamente en: data/informe_pericial.txt")

if __name__ == "__main__":
    generar_informe()
