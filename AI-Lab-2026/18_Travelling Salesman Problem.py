import itertools

def tsp(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = None
    min_cost = float("inf")

    for perm in itertools.permutations(vertices):
        cost = 0
        k = start
        for j in perm:
            cost += graph[k][j]
            k = j
        cost += graph[k][start]
        if cost < min_cost:
            min_cost = cost
            min_path = (start,) + perm + (start,)
    return min_path, min_cost

graph = {
    'A': {'B':10,'C':15,'D':20},
    'B': {'A':10,'C':35,'D':25},
    'C': {'A':15,'B':35,'D':30},
    'D': {'A':20,'B':25,'C':30}
}
print(tsp(graph,'A'))
