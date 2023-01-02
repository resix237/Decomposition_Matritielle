import numpy as np
def luDecomposition(mat, n):
 
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]
    for i in range(n):
 
        # La matrice triangulaire U 
        for k in range(i, n):
 
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
            upper[i][k] = mat[i][k] - sum
 
        # Matrice triangulaire L 
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal as 1
            else:
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])
    print("La matrice L\t\t\t\tLa matrice U")
 
    # Affichage du resultat:
    for i in range(n):
 
        # Lower
        for j in range(n):
            print(lower[i][j], end="\t")
        print("", end="\t")
 
        # Upper
        for j in range(n):
            print(upper[i][j], end="\t")
        print("")

if __name__=="__main__":
    A=np.array([[2,4,-4,1],
                [3,6,1,-2],
                [-1,1,2,3],
                [1,1,-4,1]], dtype=float)
    luDecomposition(A,A.shape[0])





#def decomposition(A):
#    y=A
#    for k in range(A.shape[0]):
#        for i in range( k+1,A.shape[0]):
#            y[i][k]=y[i][k]/y[k][k]
#            for j in range(k+1 ,A.shape[0]):