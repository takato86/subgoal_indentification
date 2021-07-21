import pandas as pd
import networkx as nx
import os


def main():
    edge_list = pd.read_csv(os.path.join("in", "four-rooms.csv"))
    G = nx.from_pandas_edgelist(edge_list, edge_attr="capacity")
    node_set = nx.minimum_node_cut(G, s=0, t=103)
    print(node_set)
    edge_set = nx.minimum_edge_cut(G, s=0, t=103)
    print(edge_set)
    cut_value, partition = nx.minimum_cut(G, _s=0, _t=103)
    print(cut_value)
    print(partition)

if __name__ == "__main__":
    main()
