from tme2 import *
# io = MyIO()

# l=io.readLinks("fucklinks.txt")
#s=Support("fucklinks.txt")

# T = [[1,2],[3,4]]
# P = [0.5,0.7]
# print(s.matVectProd(T,P,2))
# print(s.norm(P,2))
# Q = s.normalize(P,2)
# print(Q)
# T = s.getTMat()
# s.printMat(T)

pr = PageRank("fucklinks.txt")
p = pr.powerIteration(0.2, 10000)
print(p)
print(sum(p))
pr.printcheck()