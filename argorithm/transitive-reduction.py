import networkx as nx
# Tạo đồ thị
G = nx.DiGraph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_edges_from([('A', 'B'),('A', 'B'),('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')])

# Áp dụng thuật toán transitive reduction
G_trans = nx.transitive_reduction(G)

# In đồ thị kết quả
print("Các cạnh sau khi áp dụng transitive reduction")
print(G_trans.edges())

# Danh sách các cạnh bị xóa
removed_edges = list(set(G.edges()) - set(G_trans.edges()))

# In kết quả
print("Các cạnh bị xóa là:")
print(removed_edges)