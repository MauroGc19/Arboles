class BTreeNode:
    def __init__(self, new_data):
        self.data = new_data
        self.left_node = None
        self.right_node = None

class BTree:
    def __init__(self, new_data):
        self.root_node = BTreeNode(new_data)
        
    def insert(self, new_data):
        temp_node = self.root_node #Almacena la raiz en la variable temp_node
        is_complete = False
        while not is_complete:
            if new_data < temp_node.data: #Revisa si la nueva información que se le inserta es menor a la información de la temp_node
                if temp_node.left_node: #Si la raíz tiene un nodo izquierdo, se asigna a ese nodo izquierdo
                    temp_node = temp_node.left_node
                else: 
                    temp_node.left_node = BTreeNode(new_data) #Si no tiene el nodo izquierdo, asigna el nuevo nodo con la información a esa posición (izquierda), y cambia el estado de is_complete a verdadero
                    is_complete = True
            else: #Si la información del nuevo nodo es mayor
                if temp_node.right_node: #Si la raíz tiene un nodo a la derecha, temp_node se asigna a ese nodo derecho
                    temp_node = temp_node.right_node
                else: #Si no tiene el nodo derecho, asigna el nuevo nodo a la derecha de la raíz
                    temp_node.right_node = BTreeNode(new_data)
                    is_complete = True

    def preorder(self):
        self._preorder(self.root_node)
    def _preorder(self, temp_root_node):
        print(temp_root_node.data)
        if temp_root_node.left_node is not None:
            self._preorder(temp_root_node.left_node)
        if temp_root_node.right_node is not None:
            self._preorder(temp_root_node.right_node)
    def inorder(self):
        self._inorder(self.root_node)
    def _inorder(self, temp_root_node):
        if temp_root_node.left_node is not None:
            self._inorder(temp_root_node.left_node)
        print(temp_root_node.data)
        if temp_root_node.right_node is not None:
            self._inorder(temp_root_node.right_node)
    def postorder(self):
        arreglo=[]
        return self._postorder(self.root_node,arreglo)
    def _postorder(self, temp_root_node, arreglo):
        if temp_root_node.left_node is not None:
            self._postorder(temp_root_node.left_node,arreglo)
        if temp_root_node.right_node is not None:
            self._postorder(temp_root_node.right_node,arreglo)
        arreglo.append(temp_root_node.data)
        # _IsFull es una funcion que mide la cantidad de nodos tiene un arbol
    def _IsFull(self, temp_root_node, suma):
        suma= suma+1
        if temp_root_node.left_node is not None:
            suma=self._IsFull(temp_root_node.left_node, suma)
        if temp_root_node.right_node is not None:
            suma=self._IsFull(temp_root_node.right_node, suma )
        return suma
    # _nivel es una funcion que me dice el nivel del arbol para que sea completo
    def _nivel(self,temp_root_node, suma):
        suma= suma+1
        if temp_root_node.left_node is not None:
            suma =self._nivel(temp_root_node.left_node, suma)
        return suma
    def nivelcomplete(self, suma):
       if self.root_node.right_node is not None:
           suma= self._nivelcomplete(self.root_node.right_node, suma)
           return suma
    
    def _nivelcomplete(self,temp_root_node, suma ):
        suma= suma+1
        if temp_root_node.left_node is not None:
            suma =self._nivel(temp_root_node.left_node, suma)
        return suma
    def _iscomplete(self, temp_root_node, suma):
        suma= suma+1
        if temp_root_node.left_node is not None:
            suma=self._IsFull(temp_root_node.left_node, suma)
        if temp_root_node.right_node is not None:
            suma=self._IsFull(temp_root_node.right_node, suma )
        return suma