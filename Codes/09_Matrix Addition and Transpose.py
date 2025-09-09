# Perform matrix addition and find the transpose.
def mat_add(mat1,mat2):
    r=len(mat1)
    c=len(mat1[0])
    mat3=[[0 for _ in range(c)]for _ in range(r)]
    for i in range(r):
        for j in range(c):
            mat3[i][j]=mat1[i][j]+mat2[i][j]
    return mat3

def Transpose(mat):
    r=len(mat)
    c=len(mat[0])
    transposed = [[0 for _ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            transposed[j][i] = mat[i][j]
    return transposed

r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
print("Enter Matrix 1: ")
matrix1=[[int(input(f"Enter at pos {i,j}")) for j in range(c)] for i in range(r)]
print("Enter Matrix 2: ")
matrix2=[[int(input(f"Enter at pos {i,j}")) for j in range(c)] for i in range(r)]
print("Matrix 1 is:")
for row in matrix1:
    print(row)
print("Matrix 2 is:")
for row in matrix2:
    print(row)
print("Sum of two matrices is:")
for row in mat_add(matrix1,matrix2):
    print(row)
print("Transpose of Matrix 1 is:")
for row in Transpose(matrix1):
    print(row)