import numpy as np
import matplotlib.pyplot as plt


class Edge:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Node:
    
    def __init__(self, idn):
        self.idn = idn
        self.nextn = None
        self.d = 0
        self.v = False
    def copyn(self):
        n= Node(self.idn)
        n.d=self.d
        n.v = self.v
        if(self.nextn != None):
            n.nextn = self.nextn.copyn()
        return n
    def getDegree(self):
        nod = self.copyn()
        d = 0
        while(nod.nextn != None):
            d = d+1
            nod = nod.nextn  
        return d
class MyIO:
        
    def readLinks(self, s):
        listy = []
        f = open(s, "r")
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            e = Edge(int(temp[0]), int(temp[1]))
            listy.append(e)
        f.close()
        print("number of edges: " + str(self.nedges(listy)))
        print("number of nodes: " + str(self.nnodes(listy))+"\n\n")
        return listy
    
    
    def makeInputArray(self, s, n):
        listy = []
        res = np.zeros(n)
        f = open(s, "r")
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            listy.append(temp[1])
        f.close()
        for i in range(n):
             res[i] = listy.count(i)           
        return res
    
    def makeOutputArray(self, s, n):
        listy = []
        res = np.zeros(n)
        f = open(s, "r")
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            listy.append(temp[0])
        f.close()
        for i in range(n):
             res[i] = listy.count(i) 
        return res
    
    
    def nedges(self,listy):
        return len(listy)
    def nnodes(self,listy):
        s= 0
        for n in listy:
            if(s<n.x):
                s=n.x
            if(s<n.y):
                s=n.y
        return s+1
    
class Support:
    
    def __init__(self,s):
        io = MyIO()
        self.edges = io.readLinks(s)
        self.n = io.nnodes(self.edges)
        
    def matVectProd(self,T,P,n):
        Q = np.zeros(n)
        for i in range(n):
            for j in range (n):
                Q[i] = Q[i] + (T[i][j])*(P[j])
        return Q

    def normalize(self,P,n):
        v = (1-sum(P))/n
        Q = np.zeros(n)
        for i in range(n):
            Q[i]=P[i]+v
        return Q
    def mkadjarray2(self):
        listy = {}
        for i in range(self.n):
            listy[i] = (Node(i))
        for k in self.edges:
            self.put_node(listy[k.x],k.y)
        return listy
    def put_node(self,n,x):
        temp = n
        while(temp.nextn != None):
            temp = temp.nextn
        temp.nextn = Node(x)

            
    def getTMat(self):
        adjarray = self.mkadjarray2()
        T = np.zeros([self.n, self.n])
        u = -1
        d = -1
        for e in self.edges:
            
            if(u != e.x):
                u = e.x
                d = 1/(adjarray[u].getDegree())
            T[e.y][e.x] = d
        f = 1/self.n
        for i in range(self.n):
            if(adjarray[i].getDegree()==0):
                for j in range(self.n):
                    T[j][adjarray[i].idn]=f
                    
        return T
        
    def printMat(self,T):
        s = ""
        for i in range(self.n):
            for j in range(self.n):
                s = s+ str(T[i][j])+" "
            s = s+ "\n"
        print(s)

class PageRank:
    def __init__(self, s):
        self.s = Support(s)
    
    def powerIteration(self, alpha, t):
        trans = self.s.getTMat()
        p = np.zeros(self.s.n)
        v = 1/self.s.n
        for i in range(self.s.n):
            p[i] = v
            
        for k in range(t):
            p = self.s.matVectProd(trans, p, self.s.n)
            for i in range(self.s.n):
                p[i] = p[i]*(1-alpha) + alpha*v
            p = self.s.normalize(p,self.s.n)
        return p
    
    
    
    def rootedPowerIteration(self, alpha, t, p0p):
        trans = self.s.getTMat()
        p = np.zeros(self.s.n)
        p0 = np.zeros(self.s.n)
        p0[p0p] = 1
        v = 1/self.s.n
        for i in range(self.s.n):
            p[i] = v
            
        for k in range(t):
            p = self.s.matVectProd(trans, p, self.s.n)
            for i in range(self.s.n):
                p[i] = p[i]*(1-alpha) + alpha*p0[i]
            p = self.s.normalize(p,self.s.n)
        return p
    
    
    
    
    
    
    def printcheck(self):
        r = np.zeros(20)
        for e in self.s.edges:
            r[e.y]=r[e.y]+1
        s = sum(r)
        for i in range(20):
            r[i] = r[i]/s
        print(r)
        
        
class PlotDrawer:
    
    def __init__(self, s):
        io = MyIO()
        self.pgrk = PageRank(s)
        self.inputArr = io.makeInputArray(s, self.pgrk.s.n)
        self.outputArr = io.makeOutputArray(s, self.pgrk.s.n)
        
        
    def drawInplot(self):
        x = self.pgrk.powerIteration(0.15, 100)
        y = self.inputArr
        plt.scatter(x, y)
        plt.show
        
        
    
            