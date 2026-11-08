import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data
import json

with open('data/grafo_forense.json', 'r') as f:
    d = json.load(f)

mapeo = {n["id"]: i for i, n in enumerate(d["nodos"])}
edge_index = []
for a in d["aristas"]:
    if a["source"] in mapeo and a["target"] in mapeo:
        edge_index.append([mapeo[a["source"]], mapeo[a["target"]]])

edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()
x = torch.randn((len(mapeo), 16), dtype=torch.float)
data = Data(x=x, edge_index=edge_index)

class GCN(torch.nn.Module):
    def __init__(self, in_c, out_c):
        super().__init__()
        self.conv1 = GCNConv(in_c, 2 * out_c, cached=True)
        self.conv2 = GCNConv(2 * out_c, out_c, cached=True)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        return self.conv2(x, edge_index)

model = GCN(16, 32)
opt = torch.optim.Adam(model.parameters(), lr=0.01)

for ep in range(1, 6):
    model.train()
    opt.zero_grad()
    z = model(data.x, data.edge_index)
    loss = torch.norm(z, p=2) 
    loss.backward()
    opt.step()
    print(f"Epoca {ep}, Loss: {loss.item():.4f}")
