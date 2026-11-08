import json
import networkx as nx
import matplotlib.pyplot as plt

with open('data/grafo_forense.json', 'r') as f:
    d = json.load(f)

G = nx.DiGraph()
for n in d["nodos"]:
    G.add_node(n["id"], tipo=n["tipo"])
for e in d["aristas"]:
    G.add_edge(e["source"], e["target"])

centralidad = nx.betweenness_centrality(G)

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, k=0.5, seed=42)

colores = []
tamanos = []
for node in G.nodes():
    tipo = G.nodes[node]['tipo']
    if tipo == 'Persona': colores.append('#d62728')
    elif tipo == 'Cuenta': colores.append('#2ca02c')
    elif tipo == 'Empresa': colores.append('#ff7f0e')
    else: colores.append('#1f77b4')
    tamanos.append(300 + (centralidad[node] * 5000))

nx.draw_networkx_nodes(G, pos, node_color=colores, node_size=tamanos, alpha=0.8)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=8)

plt.axis('off')
plt.savefig('data/red_forense.png', format='PNG', dpi=300, bbox_inches='tight')
print("Grafico guardado.")
