from BTree import BTree
def print_node(node):
    if (node is not None):
        print("Node [Address: " + str(id(node)) + "]")
        print("- Data: " + str(node.data))
        if node.left_node is not None:
            print ("- Left node: [Address: " + str(id(node.left_node)) + "]")
        else:
            print("- Left node: [Address: None]")
        if node.right_node is not None:
            print ("- Right node: [Address: " + str(id(node.right_node)) + "]")
        else:
            print("- Right node: [Address: None]")
        print("\n")
    else:
        print("Node [Address: None]")

tree = BTree(5)
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.insert(7)
tree.insert(6)
tree.insert(8)
suma=1
# Nivel =tree._nivel(tree.root_node, suma)
# Nodos=tree._IsFull(tree.root_node, suma)
# # esa ecuacion me da el numero total de nodos que deberia tener el arbol para que sea lleno
# Nivel= (pow(2,Nivel)-1)
# if(Nodos==Nivel):
#     print("IS Full")
print(tree.nivelcomplete(suma))


# # print_node(tree.root_node)
# # print_node(tree.root_node.left_node)
# # print_node(tree.root_node.right_node)
# # print("Pre-orden")
# # tree.preorder()
# # print("In-orden")
# # tree.inorder()
# print("Post-orden")
# print(tree.postorder())
