def alphabeta(node, depth, alpha, beta, maximizingPlayer, values):
    if depth==0 or node>=len(values):
        return values[node]
    if maximizingPlayer:
        v = -999
        for i in range(2):
            v = max(v, alphabeta(node*2+i, depth-1, alpha, beta, False, values))
            alpha = max(alpha,v)
            if beta<=alpha: break
        return v
    else:
        v = 999
        for i in range(2):
            v = min(v, alphabeta(node*2+i, depth-1, alpha, beta, True, values))
            beta = min(beta,v)
            if beta<=alpha: break
        return v

values = [3,5,6,9,1,2,0,-1]
print("Alpha-Beta result:", alphabeta(0,3,-999,999,True,values))
