from tme2 import *


class PageRank:
    def __init__(self, s):
        self.s = Support(s)
    
    def powerIteration(self, alpha, t):
        trans = self.s.getTMat()
        p = [[0 for i in range(self.s.n)] for j in range(self.s.n)]
        for i in range(self.s.n):
            p[i][i] = 1/self.s.n
        for j in range(self.s.n):
            p = self.s.matVectProd(trans, p)
            for i in range(self.s.n):
                for k in range(self.s.n):
                    if i == k:
                        p[i][k] = (1 - alpha) * p[i][k] + alpha
                    else:
                        p[i][k] = (1 - alpha) * p[i][k]
            p = self.s.normalize(p)
        return p
    
    
    def powerIteration(self, g, p0, alpha, t):
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