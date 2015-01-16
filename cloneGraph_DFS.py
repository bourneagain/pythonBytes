class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

#using DFS 
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    seen={}
    seen[None] = None
    def cloneGraph(self, node):
        head = UndirectedGraphNode(node.label)
        Solution.seen[node] = True
        for n in node.neighbors:
        	if n not in Solution.seen:
        		nei = self.cloneGraph(n)
        		head.neighbors.append(nei)
        	else:
        		head.neighbors.append(n)
        return head

A=UndirectedGraphNode(2)
B=UndirectedGraphNode(3)
C=UndirectedGraphNode(4)
A.neighbors.append(B)
A.neighbors.append(C)
B.neighbors.append(C)

N=Solution()
for i in N.cloneGraph(A).neighbors:
	print i.label







