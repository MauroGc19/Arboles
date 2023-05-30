class DLLNode:
    def __init__(self, new_data):
        self.data = new_data
        self.prev_node = None
        self.next_node = None
    def insert_after(self, other_node):
        if self.next_node == None:
            self.next_node = other_node
            other_node.prev_node = self
        else:
            self.prev_node=self.next_node
            self.next_node=other_node
            