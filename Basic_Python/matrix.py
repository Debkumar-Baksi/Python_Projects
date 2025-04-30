matrix_a=[[1,2],[1,2]]
matrix_b=[[2,1],[2,1]]
matrix_c=[[0,0],[0,0]]

matrix_c[0][0]=matrix_a[0][0]*matrix_b[0][0] + matrix_a[0][1]*matrix_b[1][0]
matrix_c[0][1]=matrix_a[0][0]*matrix_b[0][1] + matrix_a[0][1]*matrix_b[1][1]
matrix_c[1][0]=matrix_a[1][0]*matrix_b[0][0] + matrix_a[1][1]*matrix_b[1][0]
matrix_c[1][1]=matrix_a[1][0]*matrix_b[0][1] + matrix_a[1][1]*matrix_b[1][1]

print(matrix_c[0][0] , matrix_c[0][1] , matrix_c[1][0] , matrix_c[1][1])