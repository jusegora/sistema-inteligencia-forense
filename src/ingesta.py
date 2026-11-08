import json
import random
import pandas as pd
import networkx as nx
import os

# Configuracion de la simulacion (Basada en esquemas de redes ilicitas documentadas)
random.seed(101)
NUM_PERSONAS = 200
NUM_CUENTAS = 100
NUM_EMPRESAS = 50

def generar_datos():
    print("Generando estructura de red...")
    
    nodos = []
    aristas = []
    
    # Crear Personas
    for i in range(NUM_PERSONAS):
        nodos.append({"id": f"P_{i}", "tipo": "Persona", "peligrosidad": random.uniform(0, 1)})
        
    # Crear Cuentas
    for i in range(NUM_CUENTAS):
        nodos.append({"id": f"C_{i}", "tipo": "Cuenta", "saldo": random.randint(1000, 50000)})
        
    # Crear Empresas
    for i in range(NUM_EMPRESAS):
        nodos.append({"id": f"E_{i}", "tipo": "Empresa", "activos": random.randint(50000, 200000)})
        
    # Crear Aristas (Transacciones y Vínculos)
    for _ in range(1500):
        origen = random.choice(nodos)
        destino = random.choice(nodos)
        
        if origen["id"] != destino["id"]:
            # Evitar conexiones ilogicas (ej. Cuenta -> Cuenta, Empresa -> Persona)
            if origen["tipo"] == "Persona" and destino["tipo"] in ["Cuenta", "Empresa"]:
                aristas.append({"source": origen["id"], "target": destino["id"], "tipo": "Control"})
            elif origen["tipo"] == "Empresa" and destino["tipo"] == "Cuenta":
                aristas.append({"source": origen["id"], "target": destino["id"], "tipo": "Transaccion", "monto": random.randint(100, 10000)})
            elif origen["tipo"] == "Persona" and destino["tipo"] == "Persona":
                aristas.append({"source": origen["id"], "target": destino["id"], "tipo": "Comunicacion"})

    os.makedirs('data', exist_ok=True)
    with open('data/grafo_forense.json', 'w') as f:
        json.dump({"nodos": nodos, "aristas": aristas}, f)
        
    print(f"Datos generados: {len(nodos)} nodos, {len(aristas)} aristas.")

def analizar_metricas():
    print("Calculando metricas de centralidad...")
    with open('data/grafo_forense.json', 'r') as f:
        datos = json.load(f)
        
    G = nx.DiGraph()
    for n in datos["nodos"]:
        G.add_node(n["id"], tipo=n["tipo"])
    for e in datos["aristas"]:
        G.add_edge(e["source"], e["target"])
        
    # Calcular centralidad de intermediacion (Betweenness)
    centralidad = nx.betweenness_centrality(G)
    
    # Extraer los 5 nodos mas importantes
    top_nodos = sorted(centralidad.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Top 5 Nodos Criticos (Intermediarios):")
    for nodo, score in top_nodos:
        print(f"  - {nodo}: {score:.4f}")
        
    # Guardar matriz para la GNN
    df = pd.DataFrame(list(G.edges()), columns=['source', 'target'])
    df.to_csv('data/aristas.csv', index=False)
    print("Estructura de red guardada para el modelo de IA.")

if __name__ == "__main__":
    generar_datos()
    analizar_metricas()
