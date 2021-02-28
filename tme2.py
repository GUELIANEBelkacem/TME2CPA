import numpy as np


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
                Q[i] = Q[i] + T[i][j]*P[j]
        return Q
    def norm(self,P,n):
        s=0
        for i in range(n):
            s = s+P[i]
        return s
    def normalize(self,P,n):
        v = (1-self.norm(P,n))/n
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
            T[e.x][e.y] = d
        f = 1/self.n
        for i in range(self.n):
            if(adjarray[i].getDegree()==0):
                for j in range(self.n):
                    T[adjarray[i].idn][j]=f
                    
        return T
        
    def printMat(self,T):
        s = ""
        for i in range(self.n):
            for j in range(self.n):
                s = s+ str(T[i][j])+" "
            s = s+ "\n"
        print(s)
            