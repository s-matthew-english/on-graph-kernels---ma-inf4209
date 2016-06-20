import numpy as np

def ps(wgh, adj, n):
    sum  = 0
    adj_i = adj # adj_i is E^i.
    for i in range(1, n+1):
        sum += wgh(i) * adj_i
        adj_i = np.dot(adj_i, adj)
    return sum


def wgh(i):
    return 1.0 / (5 ** i)


def kernel(G1_E, G1_L, G2_E, G2_L, n):
    phi_G1 = np.dot(np.dot(G1_L, ps(wgh, G1_E, n)), G1_L.transpose())
    phi_G2 = np.dot(np.dot(G2_L, ps(wgh, G2_E, n)), G2_L.transpose())
    return np.trace(np.dot(phi_G1.transpose(), phi_G2)) # frobenius matrix product of A anb B is trace(A^T . B)


def main():
    Y_E = np.array([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]])
    E_E = np.array([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]])
    M_E = np.array([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])

    Y_L = np.array([[1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]])
    E_L = np.array([[1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    M_L = np.array([[1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]])

    print "kernel(Y, Y) =", kernel(Y_E, Y_L, Y_E, Y_L, 100)
    print "kernel(Y, E) =", kernel(Y_E, Y_L, E_E, E_L, 100)
    print "kernel(Y, M) =", kernel(Y_E, Y_L, M_E, M_L, 100)
    print "kernel(E, M) =", kernel(E_E, E_L, M_E, M_L, 100)


if __name__ == '__main__':
    main()