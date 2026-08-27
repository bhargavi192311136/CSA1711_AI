graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[], 'E':['F'], 'F':[]
}


def dfs(start, visited=set()):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for n in graph[start]:
            dfs(n, visited)

print("\nDFS:"); dfs('A')
