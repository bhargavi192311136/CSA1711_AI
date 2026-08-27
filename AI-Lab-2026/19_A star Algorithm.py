from heapq import heappop, heappush

def astar(start, goal, graph, h):
    open_list = [(h[start], 0, start, [])]
    closed = set()
    while open_list:
        f, g, node, path = heappop(open_list)
        if node == goal:
            return path+[node]
        if node in closed: continue
        closed.add(node)
        for neigh, cost in graph[node]:
            heappush(open_list, (g+cost+h[neigh], g+cost, neigh, path+[node]))

graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',1)],
    'C':[('D',1)],
    'D':[]
}
h = {'A':3,'B':2,'C':1,'D':0}
print(astar('A','D',graph,h))
