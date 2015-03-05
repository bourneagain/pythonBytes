# >> a = Node.append(None, 2)
# >> a = Node.prepend(a, 1)
# >> print a
# [ 1 2 ]

# >> b = Node.generateSequence(5)
# >> print b
# [ 1 2 3 4 5 ]



class Node:
    def __init__(self, value):
        if value <= 0:
            self.value = 0
        self.next  = None
                
    @staticmethod
    def generateSequence(self, value):
        tempNode = None
        for i in range(value,0,-1):
            tempNode = prepend(tempNode,i)
        return tempNode            
                    
                 
            
        
    @staticmethod    
    def append(self, Node,  value):
        
        # None 
        Node = prepend(Node, value)
        # 1
        # 2 3  4 5 1
        #end of list
        
        ref = Node
        
        while Node.next:
            Node = Node.next
        
        Node.next  = ref
        temp = ref.next
        ref.next = None
        return temp
            
        #end of the list 
        
        
        
        ###
        tempNode = Node(value)
        Node.next = tempNode
        return ref.next
    
    @staticmethod
    def prepend(self, Node, value):
        temp = Node(value)
        temp.next = Node
        return temp



# a  = Node.prepend(None,2)
