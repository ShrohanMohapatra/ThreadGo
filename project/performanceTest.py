from threadGo import threadMatrixProduct
from random import randint
from time import time
from matplotlib import pyplot as plt
import os
import psutil
from math import fabs
def mem_usage():
    pid = os.getpid()
    py = psutil.Process(pid)
    mem = py.memory_info()[0]/(2.**30)
    return mem
A1 = range(1,20)
B1 = [0 for i in range(1,20)]
for g in range(10):
        for i in range(1,20):
                A = [[randint(8,10) for k in range(i)] for j in range(i)]
                B = [[randint(8,10) for k in range(i)] for j in range(i)]
                handle = threadMatrixProduct(A,B,i)
                start = time()
                handle.interfaceProd()
                end = time()
                if i <= 5:
                        B1[i-1] = B1[i-1]+(end-start)*(10**3)/(i*i)
                else:
                        B1[i-1] = B1[i-1]+(end-start)*(10**3)/(i*i*i)
for i in range(1,20): B1[i-1] = B1[i-1]/10
plt.plot(A1,B1)
plt.show()
for i in range(1,20):
    A = [[randint(2,10) for j in range(i)] for k in range(i)]
    B = [[randint(2,10) for j in range(i)] for k in range(i)]
    handle = threadMatrixProduct(A,B,i)
    start = mem_usage()
    handle.matrixProduct()
    end = mem_usage()
    B1[i-1] = fabs((end-start)*2**20)
plt.plot(A1,B1)
plt.show()