from nodo import DLLnode
from nodo import DLinkedList

def print_node(node):
    print("Node [Address: "+ str(id(node))+"]")
    print("- Data: "+str(node.data))
    if node.prev_node != None:
        print("- Prev node: [Address: "+str(id(node.prev_node))+"]")
    else:
        print("- Prev node: [Address: None]")
    if node.next_node != None:
        print("- Next node: [Address: "+str(id(node.next_node))+"]")
    else:
        print("- Next node: [Address: None]")
    print("\n")
    
#test code
node = DLLnode(48)
node.insert_after(DLLnode(143))
node.insert_before(DLLnode(70))
node.insert_after(DLLnode(11))
node.insert_before(DLLnode(508))
#Find the first node
node_temp = node
while node_temp.prev_node != None:
    node_temp = node_temp.prev_node

print("Print all the nodes from the first node to the last")
print_node(node_temp)
print_node
while node_temp.next_node != None:
    node_temp = node_temp
list=DLinkedList()
list.add(35)
list.add(50)
print(list.get_size())
# node = DLLnode(40)
# node2 = DLLnode(143)
# node3 = DLLnode(70)
# print_node(node)
# print_node(node2)
# node.insert_after(node2)
# print_node(node)
# print_node(node2)
# node.insert_after(node3)
# print_node(node)
# print_node(node2)
# print_node(node3)