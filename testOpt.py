# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:01:20 2021

@author: Belkacem GUELIANE & Jae-Soo LEE
"""

import time
from tme2Opt import *
from collections import defaultdict
from pympler import asizeof
import heapq
#creating EdgeList and AdjArray (also AdjMatrix but it's not scalable so it's commented out)
start = time.time()
g = Graph("amazon.txt")
l = g.mkEdgeList()
#m = g.mkAdjMatrix(l)
a = g.mkAdjarray2(l)
end = time.time()
print("creating EdgeList + AdjArray time is: "+ str(end-start)+"\n")



# running the PageRank algorithms
start = time.time()
pr = PageRank()
p = pr.powerIteration(a , 0.15, 100)
# print(p)
print("page rank time is: "+ str(end-start)+"\n")
end = time.time()

maxesid=[]
minsid=[]
maxes = heapq.nlargest(5, p)
mins = heapq.nsmallest(5, p)
for i in maxes:
    maxesid.append(p.index(i))
for i in mins:
    minsid.append(p.index(i))
print("id of max pages are:")
print(maxesid)
print("id of min pages are:")
print(minsid)
#plotting the graphs

pd = PlotDrawer(a, l, p)
pd.drawInplot()
pd.drawOutplot()
li = [0.1,0.2,0.5,0.9]
for i in li:
    pd.drawAlphaplot(a, i)



