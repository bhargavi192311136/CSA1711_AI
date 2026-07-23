from collections import deque

def bfs(start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        state = queue.popleft()
        if state == goal:
            path = []
            while state:
                path.append(state)
                state = parent[state]
            return path[::-1]

        i = state.index("0")
        moves = []
        if i not in [0,1,2]: moves.append(i-3)
        if i not in [6,7,8]: moves.append(i+3)
        if i not in [0,3,6]: moves.append(i-1)
        if i not in [2,5,8]: moves.append(i+1)

        for m in moves:
            new_state = list(state)
            new_state[i], new_state[m] = new_state[m], new_state[i]
            new_state = "".join(new_state)
            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = state
                queue.append(new_state)

start = "123405678"
goal = "123456780"
print("Solution Path:", bfs(start, goal))
