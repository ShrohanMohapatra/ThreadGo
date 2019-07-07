import unittest
from threadGo import threadMatrixProduct
from random import randint,uniform
from math import fabs
class testFramework(unittest.TestCase):
    def test_posint(self):
        n = randint(2,8)
        A = [[randint(0,10) for j in range(n)] for i in range(n)]
        B = [[randint(0,10) for j in range(n)] for i in range(n)]
        C = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n): C[i][j] = C[i][j]+A[i][k]*B[k][j]
        handle = threadMatrixProduct(A,B,n)
        handle.matrixProduct()
        trueSig = True
        for i in range(n):
            for j in range(n):
                trueSig = trueSig and handle.C[i][j] == C[i][j]
        self.assertTrue(trueSig)
    def test_int(self):
        n = randint(2,8)
        A = [[randint(-10,10) for j in range(n)] for i in range(n)]
        B = [[randint(-10,10) for j in range(n)] for i in range(n)]
        C = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n): C[i][j] = C[i][j]+A[i][k]*B[k][j]
        handle = threadMatrixProduct(A,B,n)
        handle.matrixProduct()
        trueSig = True
        for i in range(n):
            for j in range(n):
                trueSig = trueSig and handle.C[i][j] == C[i][j]
        self.assertTrue(trueSig)
    def test_posflo(self):
        n = randint(2,8)
        A = [[uniform(0,10) for j in range(n)] for i in range(n)]
        B = [[uniform(0,10) for j in range(n)] for i in range(n)]
        C = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n): C[i][j] = C[i][j]+A[i][k]*B[k][j]
        handle = threadMatrixProduct(A,B,n)
        handle.matrixProduct()
        trueSig = True
        for i in range(n):
            for j in range(n):
                trueSig = trueSig and fabs(handle.C[i][j]-C[i][j]) < 10**(-6)
        self.assertTrue(trueSig)
    def test_float(self):
        n = randint(2,8)
        A = [[uniform(-10,10) for j in range(n)] for i in range(n)]
        B = [[uniform(-10,10) for j in range(n)] for i in range(n)]
        C = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n): C[i][j] = C[i][j]+A[i][k]*B[k][j]
        handle = threadMatrixProduct(A,B,n)
        handle.matrixProduct()
        trueSig = True
        for i in range(n):
            for j in range(n):
                trueSig = trueSig and fabs(handle.C[i][j]-C[i][j]) < 10**(-6)
        self.assertTrue(trueSig)
if __name__ == '__main__':
    unittest.main()