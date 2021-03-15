# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:01:20 2021

@author: Belkacem GUELIANE & Jae-Soo LEE
"""
from collections import defaultdict
import matplotlib.pyplot as plt


class Edge:
    __slots__ = 'x', 'y'
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    
class Node:
    __slots__ = 'idn', 'neighbours'
    def __init__(self, idn):
        self.idn = idn
        self.neighbours = []

        
    def copyn(self):
        n= Node(self.idn)
        n.neighbors = self.neighbors[:]
        return n
    
    @property
    def d(self):
        return len(self.neighbours)

    
        
        
class Graph:
    """ class Graph(String s) takes the path to the .txt file containing a list of edges.
        \n contains methids for generating an Edge List, an Adjacency Matrix and/or 
        an Adjacency Array, along with print methodes for all 3 data structures"""
    def __init__(self, s):
        self.s = s
        
    #data structure makers--------------------------------------------------
    
    def mkEdgeList(self):
        """ mkEdgeList() makes an edge list from the given .txt file inserted when creating an instance of Graph""" 
        listy = []
        f = open(self.s, "r")
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            e = Edge(int(temp[0]), int(temp[1]))
            listy.append(e)
        f.close()
        print("number of edges: " + str(self.nedges(listy)))
        print("number of nodes: " + str(self.nnodes(listy))+"\n\n")
        return listy
    
    
    
    
    def mkAdjMatrix(self, l):
        """ mkAdjMatrix(EdgeList l) makes an adjacincy matrix from a given edge list""" 
        n = self.nnodes(l)
        matrix = [ [ 0 for i in range(n) ] for j in range(n) ] 
        for e in l:
            matrix[e.x][e.y] = 1
        return matrix
    
    
    
    
    def mkAdjArray(self,l):
        """ mkAdjArray(EdgeList l) makes an adjacincy array from a given edge list""" 
        
        listy = {}
        n = self.nnodes(l)
        for i in range(n):
            listy[i] = (Node(i))
        for k in l:
            listy[k.x].neighbours.append(k.y)
            listy[k.y].neighbours.append(k.x)
        return listy
    

    
    
    def mkAdjarray2(self, l):
        """ mkAdjArray2(EdgeList l) makes an adjacincy array from a given edge list 
        with the particulatity of it turned into a directed graph 
        (useful for detecting triangles)""" 
        listy = {}
        n = self.nnodes(l)
        for i in range(n):
            listy[i] = (Node(i))
        for k in l:
            listy[k.x].neighbours.append(k.y)

        return listy
    
            
    #support functions------------------------------------------------------                     
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
    
    #prints-----------------------------------------------------------------
    def print_edges(self, listy):
        f = open("EdgeList.txt", "w")
        for e in listy:
            f.write(str(e.x)+"   "+str(e.y)+"\n")
        f.close()    
    def print_matrix(self, matrix):
        f = open("AdjMatrix.txt", "w")
        s = ""
        f.write("the adjacency matrix:\n")
        s = ""
        for i in matrix:
            for j in i:
                s= s+(str(j) + " ")
            s= s+("\n")
            f.write(s)
        
        f.close() 
        
    def print_adjarray(self, listy):
        f = open("AdjArray.txt", "w")
        s = ""
        print("the adjacency array:\n")
        for i in listy:
            n = listy[i]
            s = ""
            s = s+str(n.idn)+" -> "            
            for neighbour in n.neighbours:
                s = s+str(neighbour)+" -> "
            s = s+"/\n"
            f.write(s)
            #print(s)
        f.close()
        

        
class Support:
    """ matVectProd(Transition T, Vect P, AdjArray a, Int n) simulates the 
    Matrix-Vector product and returns the resulting vector"""
    def matVectProd(self,T,P,a,n):
        Q = [ 0 for i in range(n) ]

        for i in range(n):
            if (a[i].d == 0):
                for j in range(n):
                    Q[j] = Q[j] + (T[j])*(P[i])
            
            else:
                for aa in a[i].neighbours:
                    Q[aa] = Q[aa] + (T[aa])*(P[i])
        return Q

    def normalize(self,P,n):
        v = (1-sum(P))/n
        Q = [ 0 for i in range(n) ]
        for i in range(n):
            Q[i]=P[i]+v
        return Q
            

    def getTMat(self, adjarray):
        """getTMat(AdjArray a) generates the transition matrix of a graph from an edge list""" 

        n = len(adjarray)
        T = {}
        fr = 1/n
        for i in range(n):
            d = adjarray[i].d
            if(d == 0):
                T[i] = fr
            else:
                T[i] = 1/d
        #print(T)
        return T
    
    
    def printMat(self,T):
        s = ""
        for i in range(self.n):
            for j in range(self.n):
                s = s+ str(T[i][j])+" "
            s = s+ "\n"
        print(s)

        
class PageRank:

    def powerIteration(self, a, alpha, t):
        """powerIteration(AdjArray a, Float alpha, Int iterations) the Page Rank 
        algorithm takes an AdjArray of a graph, a value alpha (0<alpha<1) 
        and a number of iterations and returns a vector that contains a pagerank value 
        for each node in the graphe""" 
        s = Support()
        n = len(a)
        trans = s.getTMat(a)
        p = [ 0 for i in range(n) ]
        #p = defaultdict(int)  
        v = 1/n
        for i in range(n):
            p[i] = v
            
        for k in range(t):
            p = s.matVectProd(trans, p, a, n)
            for i in range(n):
                
                p[i] = p[i]*(1-alpha) + alpha*v
            p = s.normalize(p, n)
        return p
    
    
    
    def rootedPowerIteration(self, a, alpha, t, p0p):
        """rootedPowerIteration(AdjArray a, Float alpha, Int iterations, Int p0) the Page Rank 
        algorithm takes an AdjArray of a graph, a value alpha (0<alpha<1) 
        and a number of iterations and returns a vector that contains a pagerank value 
        for each node in the graphe""" 
        s = Support()
        n = len(a)
        trans = s.getTMat(a)
        p = defaultdict(int) 
        p0 = defaultdict(int) 
        p0[p0p] = 1
        v = 1/n
        for i in range(n):
            p[i] = v
            
        for k in range(t):
            p = s.matVectProd(trans, p, a, n)
            for i in range(n):
                p[i] = p[i]*(1-alpha) + alpha*p0[i]
            p = s.normalize(p,n)
        return p
    
class PlotDrawer:
    """a class for drawing the graphs""" 
    def __init__(self, a, e, p):
        self.pgrk = PageRank()
        g = Graph("")
        self.n = len(a)
        self.x = p
        #self.xp = self.pgrk.rootedPowerIteration(a, 0.15, 2, 3) 
        temp = self.makeInOutArray(e, self.n)
        self.inputArr = temp[0]
        self.outputArr = temp[1]
        
        
    def drawInplot(self):
        plt.figure()
        plt.scatter(self.x, self.inputArr)
        plt.title("in-degree to pagerank")
        plt.xlabel("PageRank")
        plt.ylabel("in-degree")
        plt.show
    def drawOutplot(self):
        plt.figure()
        plt.scatter(self.x, self.outputArr)
        plt.title("out-degree to pagerank")
        plt.xlabel("PageRank")
        plt.ylabel("out-degree")
        plt.show
        plt.figure()
    def drawAlphaplot(self, a, alpha):
        y = self.pgrk.powerIteration(a, alpha, 2) 
        plt.scatter(self.x, y, label=str(alpha))
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
        # red_patch = mpatches.Patch(label=str(alpha))
        # plt.legend(handles=[red_patch])
        plt.title("pagerank by alpha variation")
        plt.xlabel("PageRank alpha = 0.15")
        plt.ylabel("PageRank variable alpha")
        plt.show
    
    
    def makeInOutArray(self, e, n):
        outp = []
        inp = []
        resout = [ 0 for i in range(n) ]
        resin = [ 0 for i in range(n) ]
        for ee in e:
            outp.append(ee.x)
            inp.append(ee.y)
        for i in range(n):
             resout[i] = outp.count(i)
             resin[i] = inp.count(i)
        return [resin, resout]

            
            
    
