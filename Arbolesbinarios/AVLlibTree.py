class AVLTreeNode:
    def __init__(self, new_data):
        self.data=new_data
        self.left_node =None
        self.right_node =None
        self.height =1
class AVLTree:
    def __init__(self, new_data):
        self.root_node =AVLTreeNode(new_data)
    def insert(self, new_data):
        temp_node = self.root_node #Almacena la raiz en la variable temp_node
        is_complete = False
        while not is_complete:
            if new_data < temp_node.data: #Revisa si la nueva información que se le inserta es menor a la información de la temp_node
                if temp_node.left_node: #Si la raíz tiene un nodo izquierdo, se asigna a ese nodo izquierdo
                    temp_node = temp_node.left_node
                else: 
                    temp_node.left_node = AVLTreeNode(new_data) #Si no tiene el nodo izquierdo, asigna el nuevo nodo con la información a esa posición (izquierda), y cambia el estado de is_complete a verdadero
                    is_complete = True
            else: #Si la información del nuevo nodo es mayor
                if temp_node.right_node: #Si la raíz tiene un nodo a la derecha, temp_node se asigna a ese nodo derecho
                    temp_node = temp_node.right_node
                else: #Si no tiene el nodo derecho, asigna el nuevo nodo a la derecha de la raíz
                    temp_node.right_node = AVLTreeNode(new_data)
                    is_complete = True