def ancestors(graph, node):
    if node in graph:
        graphs = graph[node]
        result = graphs
        for v in graphs:
            result = result + ancestors(graph,v)
        return result
    return []


ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'], 
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'], 
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'], 
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'], 
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'], 
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'], 
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'], 
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }


print ancestors(ada_family, 'Augusta Ada King')
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron', 
#    'Catherine Gordon','Captain John Byron']

#print ancestors(ada_family, 'Judith Blunt-Lytton')
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King', 
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron', 
#    'Catherine Gordon', 'Captain John Byron']

#print ancestors(ada_family, 'Dave')
#>>> []
