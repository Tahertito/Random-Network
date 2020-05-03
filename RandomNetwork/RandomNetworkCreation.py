from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as  plot
from random import random


def generate_n_isolated_nodes(number_of_nodes):
    graph = nx.Graph()
    for node in range(number_of_nodes):
        # adding just one node:
        graph.add_node("N{0}".format(node))
    return graph

def generate_random_edges(probability,graph,node_list):
    for i, node in enumerate(node_list):
        for neighbor_node in enumerate(node_list[i+1:]):
            random_prob = '{:.4f}'.format(random())
            print("random num is{}".format(random_prob))
            if float(random_prob) >= probability:
#print("nodelist:"+node_list[i][0]+" neighbor_node:"+neighbor_node[1][0])
                graph.add_edge(node_list[i][0], neighbor_node[1][0])
    return graph


graph = generate_n_isolated_nodes(100)
nodelist = list(graph.nodes(True))
graph = generate_random_edges(0.800, graph, nodelist)

print(graph.edges().__len__())
nx.draw(graph)
plot.savefig("./randomGraph.png") # save as png
plot.show()

