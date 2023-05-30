# crear el arbol
from NaryTree import *
tree = NaryTree()
# agregar algunos nodos
tree.add_node('A')
tree.add_node('B','A')
tree.add_node('C','A')
tree.add_node('D', 'B')
tree.add_node('E', 'B')
tree.add_node('F','B')
tree.add_node('G','C')
tree.add_node('H','C')
tree.add_node('I','C')
tree.add_node('J','C')
#Buscar un NODO especifico
# node = tree.find_node('B')
# print(node.data)
# tree.add_node('F','B')
# node = tree.find_node('F')
# print(node.data)
print(tree._mostrar)

