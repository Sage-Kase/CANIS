import Extract_Data
import pandas as p
import networkx as nx
import matplotlib.pyplot as plt

datas = p.read_excel('CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx')
wanted_data = ["Name (English)", "Region of Focus", "Language", "Entity owner (English)", "Parent entity (English)",
               "X (Twitter) URL",
               "X (Twitter) Follower #", "Facebook URL", "Facebook Follower #"]

list_data = []

Extract_Data.extract_all_data(datas, wanted_data, list_data)
parents = set()
graph = nx.Graph()
nodes = []
edges = []

for i in range(len(list_data)):
    curr_data = list_data[i]
# For all rows in the excel data if the data exist we add it as a node and edge for networkx
    if type(curr_data.get_value(5)) is bool and curr_data.get_value(5) is False:
        continue
    else:
        # if(curr_data.get_value(5)[1] == 0):
        #     print(curr_data.get_name())
        if curr_data.get_value(3)[1] not in parents:
            # The parent entity set and the nodes for that parent entity
            parents.add(curr_data.get_value(3)[1])
            nodes.append(curr_data.get_value(3)[1])
        edge = (curr_data.get_name(), curr_data.get_value(3)[1], curr_data.get_value(5)[1])
        nodes.append(curr_data.get_name())
        edges.append(edge)

# Making the graph (idk how to layout)
dictionary_s = graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)
pos = nx.kamada_kawai_layout(graph, scale=6000, weight="weight")
# options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}

nx.draw_networkx_nodes(graph, pos=pos)
nx.draw_networkx_labels(graph, pos=pos, labels=dictionary_s, font_family="sans-serif")
nx.draw_networkx_edges(graph, pos=pos)
#
# graph.add_weighted_edges_from(edges)
#
# pos = nx.circular_layout(graph)
# angs =
# #
plt.show()


