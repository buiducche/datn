import networkx as nx

# Tạo đồ thị
G = nx.DiGraph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_weighted_edges_from([('A', 'B', 1), ('A', 'C', 4), ('B', 'D', 2), ('C', 'D', 3), ('C', 'E', 5), ('D', 'E', 1)])
# Tìm đường đi ngắn nhất từ 'A' đến 'E'
shortest_path = nx.shortest_path(G, 'A', 'E', weight='weight')
print("Đường đi ngắn nhất:", shortest_path)