from threadGo import threadMatrixProduct
from random import randint
from time import time
def transitiveClosure(M): # M is the adjacency matrix of the graph
    # initialising the transitive closure
    T = [[0 for j in range(len(M))] for i in range(len(M))]
    # initialising an iterator
    H = [ [ M[i][j] for j in range(len(M[i]))] for i in range(len(M)) ]
    for i in range(len(M)):
        for j in range(len(M)):
            for k in range(len(M)):
                T[j][k] = T[j][k] or H[j][k]
        handle = threadMatrixProduct(H,M,len(M))
        handle.matrixProduct()
        for j in range(len(M)):
            for k in range(len(M)):
                H[j][k] = handle.C[j][k]
    for i in range(len(M)):
        for j in range(len(M)):
            T[i][j] = 1 if T[i][j]>0 else 0
    return T
n = 4 # A random choice of the number of vertices in the graph
# A random directed unweighted graph in the form of an adjacency matrix
M = [[randint(0,1) if i!=j else 0 for j in range(n)] for i in range(n)]
print("The initial adjacency matrix M is")
print(M)
H = transitiveClosure(M)
print("The adjacency matrix of the transitive closure of M is")
print(H)
print("The variation of time to calculate transitive closure with varying sizes of the input graph")
for n in range(2,11):
    M = [[randint(0,1) if i!=j else 0 for j in range(n)] for i in range(n)]
    start = time()
    H = transitiveClosure(M)
    end = time()
    print('Vertex set size',n,'Time for computation',(end-start)*10**3,'ms')