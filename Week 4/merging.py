def merge(A,B): # Merge A[0:m], B[0:n]
    (C, m, n) = ([], len(A),len(B))
    (i, j) = (0,0)
    while (i + j < m + n): # i + j is number of elements merged so far
        if (i == m): # Case 1: A is empty
            C.append(B[j])
            j = j + 1
        elif j == n: # Case 2: B is empty
            C.append(A[i])
            i = i + 1
        elif A[i] <= B[j]: # Case 3: Head of A is smaller
            c.append(A[i])
            i = i + 1
        elif A[i] >= B[j]: # Case 4: Head of B is smaller
            c.append(B[j])
            j = j + 1
        return(c)
