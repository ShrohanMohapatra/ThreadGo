from project.threadGo import threadMatrixProduct
# enter the size of the matrices
n = int(input("Enter the size of the matrix "))
# take input from user
A = []
B = []
print("Enter the elements of matrix A")
for i in range(n):
    a =[]
    for j in range(n):
        a.append(int(input())) 
    print()
    A.append(a)
print("Enter the elements of matrix B")
for i in range(n):
    a =[]
    for j in range(n):
        a.append(int(input())) 
    print()
    B.append(a)
# initialise the handle with an instance of
# class threadMatrixProduct with matrices A, B and size n
handle = threadMatrixProduct(A,B,n)
# invoke the matrix multiplication function
handle.matrixProduct()
# check out the output stored in handle.C
print("The resultant matrix is as follows ")
for i in range(n):
    for j in range(n):
        print(handle.C[i][j],end=' ')
    print()