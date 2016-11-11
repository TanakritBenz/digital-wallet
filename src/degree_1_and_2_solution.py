'''
Solution for DEGREE 1 or 2
'''

def build_graph_network(batch_input_reader):
    '''
    Build a simple graph network using a dictionary.
    Keyed by node and valued by a set of neighbors.
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    '''
    graph = dict()
    for line1, input_as_dict1 in enumerate(batch_input_reader):  # O(#lines in batch)
        id1 = input_as_dict1['id1']
        id2 = input_as_dict1['id2']

        '''
        If any node is new:
          1) Add itself the dict graph
          2) Add its friend to its neighbor set
        '''
        if id1 not in graph:
            graph[id1] = set()
        if id2 not in graph:
            graph[id2] = set()
        graph[id2].add(id1)
        graph[id1].add(id2)
    return graph

def verifier(stream_input_reader, graph, DEGREE, output_file):
    '''
    Simply check if id1 and id2 are friends by looking in theirs neighbor sets.
    If DEGREE==2, also check for their mutual friends (intersection of their 2 sets).
    After done verifying, then after update the graph for next iteration.
    '''
    for line2, input_as_dict2 in enumerate(stream_input_reader):
        result = 'unverified'
        id1 = input_as_dict2['id1']
        id2 = input_as_dict2['id2']

        # Verify transaction for degree==1
        if id1 in graph and id2 in graph:
            if id2 in graph[id1] and id1 in graph[id2]: # trusted case
                result = 'trusted'
            # elif id2 not in graph[id1] and id1 not in graph[id2]: # unverified case
            #     pass
            # else:
            #     assert (False), "nodes "+id1+" and "+id2+" must have a mutual relationship!"

            if id1 == id2:
                # Always 'trusted' a transaction between oneself
                result = 'trusted'

        # Verify transaction for degree==2 (skip if already trusted by degree==1)
        if DEGREE == 2 and result == 'unverified':
            if id1 in graph and id2 in graph:
                # Find intersection
                mutual_friends = set.intersection(graph[id1], graph[id2])
                if len(mutual_friends) > 0:
                    result = 'trusted'

        # Update the graph
        if id1 not in graph:
            graph[id1] = set()
        if id2 not in graph:
            graph[id2] = set()
        graph[id1].add(id2)
        graph[id2].add(id1)

        output_file.write(result + '\n')
