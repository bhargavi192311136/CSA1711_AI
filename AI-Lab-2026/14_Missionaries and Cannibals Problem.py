def is_valid(m,c):
    return (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)

def solve():
    from collections import deque
    start = (3,3,1)
    goal = (0,0,0)
    queue = deque([(start,[])])
    visited = set([start])
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    while queue:
        (m,c,b), path = queue.popleft()
        if (m,c,b) == goal:
            print(path+[goal]); return
        for dm,dc in moves:
            nb = 1-b
            nm = m + (-dm if b else dm)
            nc = c + (-dc if b else dc)
            state = (nm,nc,nb)
            if 0<=nm<=3 and 0<=nc<=3 and is_valid(nm,nc) and state not in visited:
                visited.add(state)
                queue.append((state,path+[state]))

solve()
