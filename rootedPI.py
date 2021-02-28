def powerIteration(g, p0, alpha, t):
    trans = transitionMatri(g)
    p = [[0 for i in range(len(g))] for j in range(len(g))]
    for i in range(len(g)):
        p[i][i] = 1/len(g)
    for j in range(len(g)):
        p = matVectProd(trans, p)
        for i in range(len(g)):
            for k in range(len(g)):
                if i == k:
                    p[i][k] = (1 - alpha) * p[i][k] + alpha * p0[i][k]
                else:
                    p[i][k] = (1 - alpha) * p[i][k]
        p = normalize2(p)
    return p