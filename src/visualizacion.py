import json
import networkx as nx
import matplotlib.pyplot as plt
import random

def generar_grafo_visual():
    print("Cargando datos de la red...")
    with open('data/grafo_forense.json', 'r') as f:
        datos = json.load(f)

    G = nx.DiGraph()
    
    # Clasificar nodos por tipo para asignar formas/colores
    for n in datos["nodos"]:
        G.add_node(n["id"], tipo=n["tipo"])
        
    for e in datos["aristas"]:
        G.add_edge(e["source"], e["target"], tipo=e["tipo"])

    # Calcular centralidad para identificar a los "capos"
    centralidad = nx.betweenness_centrality(G)
    
    # Configuración del lienzo visual
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G, k=0.5, seed=42) # Distribución de los nodos
    
    # Colores por tipo de entidad
    colores_nodos = []
    tamanos_nodos = []
    
    for node in G.nodes():
        tipo = G.nodes[node]['tipo']
        if tipo == 'Persona':
            colores_nodos.append('#d62728') # Rojo
        elif tipo == 'Cuenta':
            colores_nodos.append('#2ca02c') # Verde
        elif tipo == 'Empresa':
            colores_nodos.append('#ff7f0e') # Naranja
        else:
            colores_nodos.append('#1f77b4') # Azul
            
        # El tamaño del nodo depende de su centralidad (entre más grande, más importante)
        tamano = 300 + (centralidad[node] * 5000)
        tamanos_nodos.append(tamano)

    # Dibujar nodos y aristas
    nx.draw_networkx_nodes(G, pos, node_color=colores_nodos, node_size=tamanos_nodos, alpha=0.8)
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')

    plt.title("Visualizacion de Red Forense - Identificacion de Nodos Criticos")
    plt.axis('off')
    
    # Guardar la imagen
    plt.savefig('data/red_forense.png', format='PNG', dpi=300, bbox_inches='tight')
    print("Grafo visual guardado exitosamente en: data/red_forense.png")

if __name__ == "__main__":
    generar_grafo_visual()
