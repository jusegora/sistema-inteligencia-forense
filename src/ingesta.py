import json
import random
import pandas as pd
import networkx as nx
import os

random.seed(101)

def generar_datos():
    nodos = []
    aristas = []
    
    for i in range(200):
        nodos.append({"id": f"P_{i}", "tipo": "Persona", "peligrosidad": random.uniform(0, 1)})
    for i in range(100):
        nodos.append({"id": f"C_{i}", "tipo": "Cuenta", "saldo": random.randint(1000, 50000)})
    for i in range(50):
        nodos.append({"id": f"E_{i}", "tipo": "Empresa", "activos": random.randint(50000, 200000)})
        
    for _ in range(1500):
        ori = random.choice(nodos)
        dest = random.choice(nodos)
        
        if ori["id"] != dest["id"]:
            if ori["tipo"] == "Persona" and dest["tipo"] in ["Cuenta", "Empresa"]:
                aristas.append({"source": ori["id"], "target": dest["id"], "tipo": "Control"})
            elif ori["tipo"] == "Empresa" and dest["tipo"] == "Cuenta":
                aristas.append({"source": ori["id"], "target": dest["id"], "tipo": "Transaccion", "monto": random.randint(100, 10000)})
            elif ori["tipo"] == "Persona" and dest["tipo"] == "Persona":
                aristas.append({"source": ori["id"], "target": dest["id"], "tipo": "Comunicacion"})

    os.makedirs('data', exist_ok=True)
    with open('data/grafo_forense.json', 'w') as f:
        json.dump({"nodos": nodos, "aristas": aristas}, f)
        
    print(f"Datos generados: {len(nodos)} nodos, {len(aristas)} aristas.")

def analizar():
    with open('data/grafo_forense.json', 'r') as f:
        datos = json.load(f)
        
    G = nx.DiGraph()
    for n in datos["nodos"]:
        G.add_node(n["id"], tipo=n["tipo"])
    for e in datos["aristas"]:
        G.add_edge(e["source"], e["target"])
        
    centralidad = nx.betweenness_centrality(G)
    top = sorted(centralidad.items(), key=lambda x: x[1], reverse=True)[:5]
    
    print("Top 5 Nodos Criticos:")
    for n, score in top:
        print(f"  {n}: {score:.4f}")
        
    df = pd.DataFrame(list(G.edges()), columns=['source', 'target'])
    df.to_csv('data/aristas.csv', index=False)

if __name__ == "__main__":
    generar_datos()
    analizar()
