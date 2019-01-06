def LCS(u, v): # u[0....m-1], v[0......n-1]
    for r in range(len(u)+1):
        LCS[r][len(u)+1] = 0
    for c in range(len(v)+1):
        LCS[len(v)+1][c] = 0
    for c in range(len(v), -1, -1):
        for r in range(len(u), -1, -1):
            if(u[r] == v[c]):
                LCS[r][c] = 1 + LCS[r+1][c+1]
            else:
                LCS[r][c]=max(LCS[r+1][c], LCS[r][c+1])
    return(LCS[0][0])
