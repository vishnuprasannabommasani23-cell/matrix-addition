A=[[1,2],[3,6]]
B=[[5,9],[3,6]]
C=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]+B[i][j])
    C.append(row)
print(C)
for i in range(2):
    for j in range(2):
        print(C[i][j],end="   ")
    print()
    
                       
