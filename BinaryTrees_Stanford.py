class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    count = 0
    def addNode(self, root, data):
        if not root:
            return TreeNode(data)
        if data <= root.data:
            root.left = self.addNode(root.left,data)
        else:
            root.right = self.addNode(root.right,data)
        return root

    def findNode(self, root, data):
        if not root:
            return None
        if root.data == data:
            return root
        elif root.data <= data:
            return self.findNode(root.right,data)
        else:
            return self.findNode(root.left,data)

    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        print root.data,
        self.inorder(root.right)

    def postorder(self, root):
        if not root:
            return 
        self.postorder(root.left)
        self.postorder(root.right)
        print root.data,

    def dfs(self, root):
        if not root:
            return
        BSTree.count += 1
        if  root.left:
            self.dfs(root.left)
        if  root.right:
            self.dfs(root.right)
        return BSTree.count

    def size(self, root):
        if not root:
            return 0
        return self.size(root.left)+1+self.size(root.right)

    def max_depth(self, root):
        if not root:
            return 0
        return 1+max(self.max_depth(root.left), self.max_depth(root.right))

    def min_value(self, root):
        if not root:
            return None
        if not root.left:
            return root.data    
        else:
            return self.min_value(root.left)

    def min_value_iter(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root.data

    def print_paths(self, root):
        if not root:
            return None
        alist=[None]*100
        self.print_paths_helper(root, alist, 0)

    def print_paths_helper(self, root, alist, level):
        if not root:
            return
        alist[level] = root.data
        level+=1
        if not root.left  and not root.right:
            print alist[:level]
        else:
            self.print_paths_helper(root.left, alist, level)
            self.print_paths_helper(root.right, alist, level)

    def has_path_sum(self, root, gsum):
        if not root:
            return gsum == 0
        else:
            return  self.has_path_sum(root.left, gsum-root.data) or  self.has_path_sum(root.right, gsum-root.data) 

    def mirror(self, root):
        if not root:
            return
        temp = root.left
        root.left = self.mirror(root.right)
        root.right = self.mirror(temp)
        return root

    def mirror_inplace(self, root):
        if not root:
            return
        self.mirror(root.right)
        self.mirror(root.left)
        root.left,root.right = root.right, root.left
    
    def doubleTree(self, root):
        if not root:
            return None
        self.doubleTree(root.left)
        self.doubleTree(root.right)
        t = TreeNode(root.data)
        t.left = root.left
        root.left = t

    def same_tree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 and root2:
            return False
        elif root1 and not root2:
            return False

        if root1.data == root2.data:
            return self.same_tree(root1.left,root2.left) and  self.same_tree(root1.right,root2.right)
        else:
            return False

    def isBST(self, root):
        MIN = -999
        MAX = 999
        if not root:
            return False
        return self.isBST_helper(root, MIN, MAX)

    def isBST_helper(self, root, min_value, max_value):
        if not root:
            return True
        if root.data > max_value or root.data < min_value:
            return False
        else:
            l = self.isBST_helper( root.left, min_value, root.data)
            r = self.isBST_helper( root.right, root.data+1, max_value)
            if l and r:
                return True
            else:
                return False

    def printLevelOrder(self, root):
        import Queue
        alist = []
        if not root:
            return None
        cur_level_count = 1
        next_level_count = 0
        q = Queue.Queue()
        q.put(root)
        temp = []
        while not q.empty():
            popNode = q.get()
            cur_level_count-=1
            if popNode:
                temp.append(popNode.data)
                q.put(popNode.left)
                q.put(popNode.right)
                next_level_count+=2
            if cur_level_count == 0:
                alist.append(temp)
                cur_level_count = next_level_count
                next_level_count = 0
                temp = []
        return alist

    def lca(self, root, n1, n2):
        # idea is going from bottom 
        if not root:
            return None
        if root.data == n1 or root.data == n2:
            return root
        l = self.lca(root.left, n1, n2)
        r = self.lca(root.right, n1, n2)
        if l and r:
            return root
        else:
            return l if l else r
    def min_value_node(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root
    def delete_node(self, root, data):
        if not root:
            return None
        if root.data == data:
            if not root.left:
                temp = root.right
                del root
                return temp
            elif not root.right:
                temp = root.left
                del root
                return temp
            min_node = self.min_value_node(root.right)
            root.data = min_node.data
            root.right = self.delete_node(root.right, min_node.data )

        if root.data < data:
            root.left = self.delete_node(root.left, data)
        else:
            if root.data > data:
                root.right = self.delete_node(root.right, data)
        return root

    def sum_tree(self, root):
        if not root:
            return None
        if root.left:
            root.data+=self.sum_tree(root.left).data
        if root.right:
            root.data+=self.sum_tree(root.right).data
        return root

    def search_index(self, ino, in_start, in_end, value):
        while in_start <= in_end:
            if ino[in_start] == value:
                return in_start
            in_start+=1

    def construct_tree_inorder_preorder(self, ino, preo, instart, inend, prestart ):
        print preo, instart, inend
        if instart > inend:
            return None
        root = TreeNode(preo[prestart])
        if instart == inend:
            return root
        index = self.search_index(ino, instart, inend, root.data)
        print root.data, index
        root.left = self.construct_tree_inorder_preorder(ino, preo, instart, index,prestart+1)
        root.right = self.construct_tree_inorder_preorder(ino, preo, index+1, inend,prestart+1)
        return root





tree = BSTree()
# root = TreeNode(1)
# root.left=TreeNode(2)
# root.right=TreeNode(3)

preorder = [7,10,4,3,1,2,8,11]
inorder = [4,10,3,1,7,11,8,2]
root  = tree.construct_tree_inorder_preorder(inorder, preorder, 0 , len(inorder), 0 )
# root.right.right=TreeNode(4)

# root2 = TreeNode(2)
# root2.left=TreeNode(1)
# root2.right=TreeNode(4)

# root.left.left=TreeNode(4)
# # root.left.left.left=TreeNode(8)
# # root.left.right=TreeNode(5)
# root.right.left=TreeNode(6)
# root.right.right=TreeNode(7)
# root = tree.sum_tree(root)
tree.inorder(root)
# root = tree.delete_node(root,)
# print "DELETE"
# tree.inorder(root)
# root = tree.addNode(root, 199)
# root = tree.addNode(root, 300)
# root = tree.addNode(root, -21)
# root = tree.addNode(root, 890)
# root = tree.addNode(root, 8900)
# root = tree.addNode(root, 4)
# print tree.printLevelOrder(root)
# print tree.lca(root, 1, 1).data
# # root = tree.addNode(root, 200)
# root = tree.addNode(root, 1)
# tree.inorder(root)
# print "POST"
# tree.postorder(root)
# print "DONE"
# print tree.size(root)
# print tree.max_depth(root)
# print tree.min_value(root)
# print tree.min_value_iter(root)
# print tree.print_paths(root)
# print tree.has_path_sum(root,18)
# root = tree.mirror(root)
# tree.mirror_inplace(root)

# tree.doubleTree(root)
# print "DOYVLEDONE"
# print tree.same_tree(root1,root2)
# tree.inorder(root)
#print tree.isBST(root1)



