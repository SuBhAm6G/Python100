# Build a python program to implement Mean &
# Variance Matrix, Covariance Matrix by using python loops and list.
def mean_mat(data):
    r=len(data)
    c=len(data[0])
    mean=[]
    for i in range(r):
        sum=0
        for j in range(c):
            sum+=data[i][j]
        mean.append(sum/c)
    return mean
        
def var_mat(data):
    r=len(data)
    c=len(data[0])
    mean=mean_mat(data)
    var=[]
    for i in range(r):
        var_sum=0
        for j in range(c):
            a=(data[i][j]-mean[i])**2
            var_sum+=a
        var.append(var_sum/c)
    return var

def covar_mat(data):
    r=len(data)
    c=len(data[0])
    mean=mean_mat(data)
    covariance=[[0 for _ in range(r)] for _ in range(r)]
    for i in range(r):
        for j in range(r):
            covar_sum=0
            for k in range(c):
                covar_sum+=(data[i][k]-mean[i])*(data[j][k]-mean[j])
            covariance[i][j]=(covar_sum/c)
    return covariance

r=int(input("Rows= "))
c=int(input("Cols= "))
data=[[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        a=data[i][j]=float(input(f"Enter element [{i}][{j}]: "))
print("Data:")
for i in range(r):
    print(data[i])
print("Mean Matrix: ")
m=mean_mat(data)
print(m)
print("Var Matrix: ")
v=var_mat(data)
print([round(x,3) for x in v])
print("Covariance Matrix: ")
cov=covar_mat(data)
for row in cov:
    print([round(x,3) for x in row])
