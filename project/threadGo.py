from threading import Thread
class threadStrassenProduct():
    n = 1
    nm = 1
    A = [[0]]
    B = [[0]]
    C = [[0]]
    def __init__(self,A,B,n):
        self.nm = n
        k = 1
        while not(k >= n): k = k * 2
        self.n = k
        self.A = [
            [ ( A[i][j] if i < n and j < n else 0 )
            for j in range(k)]
            for i in range(k)]
        self.B = [
            [ ( B[i][j] if i < n and j < n else 0 )
            for j in range(k)]
            for i in range(k)]
        self.C = [[0 for j in range(k)] for i in range(k)]
    def func1(self,A11,B11,i,j,n):
        A11[i][j] = self.A[i][j]
        B11[i][j] = self.B[i][j]
    def func2(self,A12,B12,i,j,n):
        A12[i][j-int(n/2)] = self.A[i][j]
        B12[i][j-int(n/2)] = self.B[i][j]
    def func3(self,A21,B21,i,j,n):
        A21[i-int(n/2)][j] = self.A[i][j]
        B21[i-int(n/2)][j] = self.B[i][j]
    def func4(self,A22,B22,i,j,n):
        A22[i-int(n/2)][j-int(n/2)] = self.A[i][j]
        B22[i-int(n/2)][j-int(n/2)] = self.B[i][j]
    def func5(self,C11,M1,M4,M5,M7,i,j):
        C11[i][j] = M1[i][j] + M4[i][j] - M5[i][j] + M7[i][j]
    def func6(self,C12,M3,M5,i,j):
        C12[i][j] = M3[i][j] + M5[i][j]
    def func7(self,C21,M2,M4,i,j):
        C21[i][j] = M2[i][j] + M4[i][j]
    def func8(self,C22,M1,M2,M3,M6,i,j):
        C22[i][j] = M1[i][j] - M2[i][j] + M3[i][j] + M6[i][j]
    def threadAdd(self,A,B,C,i,j):
        C[i][j] = A[i][j] + B[i][j]
    def threadSub(self,A,B,C,i,j):
        C[i][j] = A[i][j] - B[i][j]
    def threadCopy(self,A,B,i,j):
        B[i][j] = A[i][j]
    def threadBucket(self,C11,C12,C21,C22,i,j):
        if i < int(self.n/2) and j < int(self.n/2):
            self.C[i][j] = C11[i][j]
        elif i < int(self.n/2) and j >= int(self.n/2):
            self.C[i][j] = C12[i][j-int(self.n/2)]
        elif i >= int(self.n/2) and j < int(self.n/2):
            self.C[i][j] = C21[i-int(self.n/2)][j]
        else:
            self.C[i][j] = C22[i-int(self.n/2)][j-int(self.n/2)]
    def matrixProduct(self):
        if self.n == 1:
            self.C[0][0] = self.A[0][0] * self.B[0][0]
            return
        A11 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        A12 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        A21 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        A22 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        B11 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        B12 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        B21 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        B22 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        C11 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        C12 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        C21 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        C22 = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D1  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D2  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D3  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D4  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D5  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D6  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D7  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D8  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D9  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        D10  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        M1  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        M2  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        M3  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        M4  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        M5  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        M6  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        M7  = [[0 for j in range(int(self.n/2))] for i in range(int(self.n/2))]
        threadList = [
            [
                [Thread(target=self.func1,args=(A11,B11,i,j,self.n,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.func2,args=(A12,B12,i,j,self.n,)) for j in range(int(self.n/2),self.n)]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.func3,args=(A21,B21,i,j,self.n,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2),self.n)
            ],
            [
                [Thread(target=self.func4,args=(A22,B22,i,j,self.n,)) for j in range(int(self.n/2),self.n)]
                for i in range(int(self.n/2),self.n)
            ]
        ]
        for i in range(4):
            for j in range(int(self.n/2)):
                for k in range(int(self.n/2)): threadList[i][j][k].start()
        for i in range(4):
            for j in range(int(self.n/2)):
                for k in range(int(self.n/2)): threadList[i][j][k].join()
        threadList = [
            [
                [Thread(target=self.threadAdd,args=(A11,A22,D1,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.threadAdd,args=(B11,B22,D2,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.threadAdd,args=(A21,A22,D3,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.threadSub,args=(B12,B22,D4,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.threadSub,args=(B21,B11,D5,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.threadAdd,args=(A11,A12,D6,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.threadSub,args=(A21,A11,D7,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.threadAdd,args=(B11,B12,D8,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.threadSub,args=(A12,A22,D9,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.threadAdd,args=(B21,B22,D10,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ]
        ]
        for i in range(10):
            for j in range(int(self.n/2)):
                for k in range(int(self.n/2)): threadList[i][j][k].start()
        for i in range(10):
            for j in range(int(self.n/2)):
                for k in range(int(self.n/2)): threadList[i][j][k].join()
        multipleThreads = [
            threadStrassenProduct(D1,D2,int(self.n/2)),
            threadStrassenProduct(D3,B11,int(self.n/2)),
            threadStrassenProduct(A11,D4,int(self.n/2)),
            threadStrassenProduct(A22,D5,int(self.n/2)),
            threadStrassenProduct(D6,B22,int(self.n/2)),
            threadStrassenProduct(D7,D8,int(self.n/2)),
            threadStrassenProduct(D9,D10,int(self.n/2))
        ]
        multiplyThreads = [
            Thread(target=multipleThreads[i].matrixProduct,args=())
            for i in range(7)
        ]
        for i in range(7): multiplyThreads[i].start()
        for i in range(7): multiplyThreads[i].join()
        threadList = [
            [
                [
                    Thread(target=self.threadCopy,args=(multipleThreads[0].C,M1,i,j,))
                    for j in range(int(self.n/2))
                ]
                for i in range(int(self.n/2))
            ],
            [
                [
                    Thread(target=self.threadCopy,args=(multipleThreads[1].C,M2,i,j,))
                    for j in range(int(self.n/2))
                ]
                for i in range(int(self.n/2))
            ],
            [
                [
                    Thread(target=self.threadCopy,args=(multipleThreads[2].C,M3,i,j,))
                    for j in range(int(self.n/2))
                ]
                for i in range(int(self.n/2))
            ],
            [
                [
                    Thread(target=self.threadCopy,args=(multipleThreads[3].C,M4,i,j,))
                    for j in range(int(self.n/2))
                ]
                for i in range(int(self.n/2))
            ],
            [
                [
                    Thread(target=self.threadCopy,args=(multipleThreads[4].C,M5,i,j,))
                    for j in range(int(self.n/2))
                ]
                for i in range(int(self.n/2))
            ],
            [
                [
                    Thread(target=self.threadCopy,args=(multipleThreads[5].C,M6,i,j,))
                    for j in range(int(self.n/2))
                ]
                for i in range(int(self.n/2))
            ],
            [
                [
                    Thread(target=self.threadCopy,args=(multipleThreads[6].C,M7,i,j,))
                    for j in range(int(self.n/2))
                ]
                for i in range(int(self.n/2))
            ]
        ]
        for i in range(7):
            for j in range(int(self.n/2)):
                for k in range(int(self.n/2)): threadList[i][j][k].start()
        for i in range(7):
            for j in range(int(self.n/2)):
                for k in range(int(self.n/2)): threadList[i][j][k].join()
        threadList = [
            [
                [Thread(target=self.func5,args=(C11,M1,M4,M5,M7,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],    
            [
                [Thread(target=self.func6,args=(C12,M3,M5,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.func7,args=(C21,M2,M4,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ],
            [
                [Thread(target=self.func8,args=(C22,M1,M2,M3,M6,i,j,)) for j in range(int(self.n/2))]
                for i in range(int(self.n/2))
            ]
        ]
        for i in range(4):
            for j in range(int(self.n/2)):
                for k in range(int(self.n/2)): threadList[i][j][k].start()
        for i in range(4):
            for j in range(int(self.n/2)):
                for k in range(int(self.n/2)): threadList[i][j][k].join()
        threadList = [
            [
                Thread(target=self.threadBucket,args=(C11,C12,C21,C22,i,j))
                for j in range(self.n)
            ]
            for i in range(self.n)
        ]
        for i in range(self.n):
            for j in range(self.n): threadList[i][j].start()
        for i in range(self.n):
            for j in range(self.n): threadList[i][j].join()
    def interfaceProd(self):
        self.matrixProduct()
        C1 = [[0 for i in range(self.nm)] for j in range(self.nm)]
        for i in range(self.nm):
            for j in range(self.nm): C1[i][j] = self.C[i][j]
        self.C = [[C1[i][j] for j in range(self.nm)] for i in range(self.nm)]
class threadNormalProduct():
    n = 1
    A = [[0]]
    B = [[0]]
    C = [[0]]
    def __init__(self,A,B,n):
        self.n = n
        self.A = [[A[i][j] for j in range(n)] for i in range(n)]
        self.B = [[B[i][j] for j in range(n)] for i in range(n)]
        self.C = [[0 for j in range(n)] for i in range(n)]
    def threadCollector(self,i,j,k):
        self.C[i][j] = self.C[i][j] + self.A[i][k] * self.B[k][j]
    def matrixProduct(self):
        threadList = [
            [
                [
                    Thread(target=self.threadCollector,args=(i,j,k,))
                    for k in range(self.n)
                ]
                for j in range(self.n)
            ]
            for i in range(self.n)
        ]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n): threadList[i][j][k].start()
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n): threadList[i][j][k].join()
class threadMatrixProduct(threadStrassenProduct,threadNormalProduct):
    n = 1
    A = [[0]]
    B = [[0]]
    C = [[0]]
    def __init__(self,A,B,n):
        self.n = n
        self.A = [[A[i][j] for j in range(n)] for i in range(n)]
        self.B = [[B[i][j] for j in range(n)] for i in range(n)]
        self.C = [[0 for j in range(n)] for i in range(n)]
    def matrixProduct(self):
        if self.n <= 4:
            handle = threadStrassenProduct(self.A,self.B,self.n)
            handle.interfaceProd()
            for i in range(self.n):
                for j in range(self.n):
                    self.C[i][j] = handle.C[i][j]
        else:
            handle = threadNormalProduct(self.A,self.B,self.n)
            handle.matrixProduct()
            for i in range(self.n):
                for j in range(self.n):
                    self.C[i][j] = handle.C[i][j]