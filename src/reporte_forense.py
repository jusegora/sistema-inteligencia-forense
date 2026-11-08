import json
import networkx as nx

with open('data/grafo_forense.json', 'r') as f:
    d = json.load(f)

G = nx.DiGraph()
for n in d["nodos"]:
    G.add_node(n["id"], tipo=n["tipo"])
for e in d["aristas"]:
    G.add_edge(e["source"], e["target"])

centralidad = nx.betweenness_centrality(G)
top = sorted(centralidad.items(), key=lambda x: x[1], reverse=True)[:5]

txt = []
txt.append("INFORME TECNICO - ANALISIS DE RED")
txt.append(f"Entidades: {len(d['nodos'])} | Relaciones: {len(d['aristas'])}")
txt.append("\nNodos Criticos:")
for i, (n, s) in enumerate(top, 1):
    txt.append(f"[{i}] {n} ({G.nodes[n]['tipo']}) - Indice: {s:.4f}")

txt.append(f"\nConclusion: El nodo '{top[0][0]}' es el eje principal de la red.")

with open('data/informe_pericial.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(txt))
print("Informe generado.")
