class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

#using DFS 
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        seen={}
        visited=[]
        seen[None] = None

        head = UndirectedGraphNode(node.label)
        seen[node] = head
        visited.append(node)
        while len(visited) != 0:
            refNode = visited.pop()
            for n in refNode.neighbors:
                if n not in seen:
                    neighBorNode = UndirectedGraphNode(n.label)
                    seen[refNode].neighbors.append(neighBorNode)
                    seen[n] = neighBorNode
                    visited.append(n)
                else:
                    seen[refNode].neighbors.append(seen[n])
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







