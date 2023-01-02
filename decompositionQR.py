import numpy as np
from scipy.linalg import qr


def QR_Decomposition(A):
    n, m = A.shape  # get the shape of A

    Q = np.empty((n, n))  # initialize matrix Q
    u = np.empty((n, n))  # initialize matrix u

    u[:, 0] = A[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])

    for i in range(1, n):

        u[:, i] = A[:, i]
        for j in range(i):
            u[:, i] -= (A[:, i] @ Q[:, j]) * Q[:, j]  # get each u vector

        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i])  # compute each e vetor

    R = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):
            R[i, j] = A[:, j] @ Q[:, i]

    print("La matrice Q\t\t\t\t\t\t\t\t\t\t\tLa matrice R")

    # Affichage du resultat:
    for i in range(n):

        # Lower
        for j in range(n):
            print(Q[i][j], end="\t")
        print("", end="\t")

        # Upper
        for j in range(n):
            print(R[i][j], end="\t")
        print("")


if __name__ == "__main__":
    A = np.array([[4, 12, -16],
                  [12, 37, -43],
                  [-16, -43, 98]], dtype=float)
    QR_Decomposition(A)
