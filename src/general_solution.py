'''
Solution for DEGREE > 2
'''

import networkx as nx

def build_graph_network(batch_input_reader):
    '''
    Build an undirected unweighted graph using networkx.
    '''
    graph = nx.Graph()
    for line1, input_as_dict1 in enumerate(batch_input_reader):  # O(#lines in batch)
        id1 = input_as_dict1['id1']
        id2 = input_as_dict1['id2']
        graph.add_edge(id1, id2)
    return graph


def verifier(stream_input_reader, graph, DEGREE, output_file):
    '''
    Using networkx's shortest_path_length method to find a shortest path between the 2 nodes.
    If the shortest path length > DEGREE or no path exists then a transaction is unverified.
    The shortest_path_length method utilizes bidirectional search algorithm.
    Runtime: O(b^(d/2)) where b = the branching factor and d = the distance from id1 to id2.
    Reference: https://en.wikipedia.org/wiki/Bidirectional_search
    After done verifying, then after update the graph for next iteration.
    '''
    for line2, input_as_dict2 in enumerate(stream_input_reader):
        result = 'unverified'
        id1 = input_as_dict2['id1']
        id2 = input_as_dict2['id2']
        has_node1 = graph.has_node(id1)
        has_node2 = graph.has_node(id2)

        if has_node1 and has_node2:
            try:
                if nx.shortest_path_length(graph, id1, id2) <= DEGREE:
                    result = 'trusted'
            except nx.NetworkXNoPath:
                pass # No path between the 2 nodes, thus result='unverified'

        graph.add_edge(id1, id2)
        output_file.write(result + '\n')
