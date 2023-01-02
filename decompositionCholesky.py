import numpy as np
import math


def cholesky_Decomposition(matrix, n):

    lower = [[0 for x in range(n + 1)]
             for y in range(n + 1)]

    # Je commence la decomposition
    # A l'interieur de L
    for i in range(n):
        for j in range(i + 1):
            sum1 = 0

            if (j == i):
                for k in range(j):
                    sum1 += pow(lower[j][k], 2)
                lower[j][j] = int(math.sqrt(matrix[j][j] - sum1))
            else:
                for k in range(j):
                    sum1 += (lower[i][k] * lower[j][k])
                if (lower[j][j] > 0):
                    lower[i][j] = int((matrix[i][j] - sum1) /
                                      lower[j][j])

    # Affichage du resultat et de ca transposee
    print("Matrice L \t\t\t\tTransposee de L ")
    for i in range(n):

        # Lower Triangular
        for j in range(n):
            print(lower[i][j], end="\t")
        print("", end="\t")

        # Transpose of
        # Lower Triangular
        for j in range(n):
            print(lower[j][i], end="\t")
        print("")


if __name__ == "__main__":
    A = np.array([[4, 12, -16],
                  [12, 37, -43],
                  [-16, -43, 98]], dtype=float)
    cholesky_Decomposition(A, A.shape[0])
