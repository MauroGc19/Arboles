
class DLLnode:
    def __init__(self,new_data):
        self.data= new_data

        self.next_node = None

        self.prev_node = None
        
    def insert_after(self, other_node):
        if self.next_node != None:
            aux_node = self.next_node
            aux_node.prev_node = other_node
            other_node.next_node = aux_node
        
        self.next_node = other_node
        other_node.prev_node = self

        return self

    def insert_before(self, other_node):
        if self.prev_node != None:
            aux_node = self.prev_node
            aux_node.next_node = other_node
            other_node.prev_node = aux_node

        self.prev_node = other_node
        other_node.next_node = self

        return self
class DLinkedList:
    def __init__(self):
           self.first_node=None
           self.last_node=None
           self.size=0
    def add(self, new_data):
        if self.first_node==None:
            self.first_node=DLLnode(new_data)
            self.last_node=self.first_node
        else:
            self.first_node.insert_after(DLLnode(new_data))
            self.last_node=self.last_node.next_node
        self.size=self.size+1
    def get_size(self):
        return self.size 
            
             





# other_node.prev_node=self
# other_node.next_node = self.next_node
# self.next_node = other_node
# other_node.next_node.prev_node= other_node