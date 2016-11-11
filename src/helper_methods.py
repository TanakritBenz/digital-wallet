import re

def replace_esc_chars(s):
    '''
    Method to remove '\t', '\r', and emoji.
    '''
    # '\t' represents tab. '\r' represents carriage return.
    s = s.replace('\t', ' ').replace('\r', ' ')
    # Remove unicode chars
    s = re.sub(r'[^\x00-\x7F]+',' ', s)
    # Convert str to unicode for StringIO
    return s.decode('utf-8')

def dfs_search_max_depth(graph, start, target, max_depth):
    '''
    Depth-Limited Depth-First Search Algorithm (Modified from naive DFS).
    Runtime: O(b^l) where b = the branching factor and l = the max depth limit.
    Has an ability to not continue searching downward when reaches max_depth.
    '''
    # print 'Start:' + start + '  Target:' + target
    visited, nodes_added_to_stack, stack = set(), set(), [(start, 0)]
    while stack:
        node, current_depth = stack.pop()
        if node == target:
            # print 'Found path to ' + target + ' from ' + start
            return True
        if node not in visited:
            visited.add(node)
            if current_depth <= max_depth:
                nodes_to_add_to_stack = graph[node] - visited - nodes_added_to_stack
                for n in nodes_to_add_to_stack:
                    nodes_added_to_stack.add(n)
                    stack.append((n, current_depth+1))
    # print 'No path from ' + start + ' to ' + target
    return False
