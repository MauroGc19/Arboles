import os
from NaryTree import NaryTree, NaryTreeNode
import tkinter as tk

class Gestor:
    def __init__(self):
        self.arbol_directorios = NaryTree()


    def explorar(self, ruta_actual,frame, padre = None,):
        lista_archivos = os.listdir(ruta_actual)
        for archivo in lista_archivos:
                ruta_completa = ruta_actual +"/"+ archivo 
                nodo = NaryTreeNode(ruta_completa)
                self.arbol_directorios.add_node(ruta_completa, ruta_actual)
                nombre=os.path.basename(nodo.data)
                nombre_padre=os.path.basename(padre)
                info_label = tk.Label(frame)
                info_label.pack()
                info_label.config(text="el nombre de la carpeta es "+ nombre+" y esta en "+nombre_padre)
                if os.path.isdir(ruta_completa):
                    self.explorar(ruta_completa,frame, nodo.data)
    def renombrar(self, ruta_original, nombre, label):
        padre=self.arbol_directorios._find_parent(ruta_original, self.arbol_directorios.root)
        if padre:
            ruta_nueva = padre.data+ "/"+nombre
            try:
                nombre_original=os.path.basename(ruta_original)
                os.rename(ruta_original, ruta_nueva)
                self.arbol_directorios.rename_node(ruta_original, ruta_nueva)
                label.config(text="La cartea '{}'fue renombrada por ".format(nombre_original)+nombre)
               
            except:
                print("Error al renombrar el archivo/carpeta.")
        else:
            print("No se encontró la ubicación original del archivo/carpeta.")
        # ruta =self.arbol_directorios.find_node(ruta_nueva)
        # print(ruta.data)
        
        
    def eliminar(self, locacion,frame):
        # nombre=os.path.basename(locacion)
        # self.arbol_directorios.remove_node(locacion)
        # if os.path.isdir(locacion):
        #      os.rmdir(locacion)
        #     #  label.config(text="La carpeta '{}' fue eliminada".format(nombre))
        # else:
        #     os.remove(locacion)
        #     print("has been removed successfully")
        #     # label.config(text="El archivo '{}' ha sido eliminado exitosamente".format(nombre))
        if os.path.isdir(locacion):
            # Eliminar directorio y su contenido
            try:
                for item in os.listdir(locacion):
                    item_path = os.path.join(locacion, item)
                    self.eliminar(item_path,frame)
                nombre=os.path.basename(locacion)
                os.rmdir(locacion)
                self.arbol_directorios.remove_node(locacion)
                info_label = tk.Label(frame)
                info_label.pack()
                info_label.config(text="La carpeta '{}' fue eliminada".format(nombre))
            except OSError as e:
                info_label = tk.Label(frame)
                info_label.pack()
                info_label.config(text=f"No se pudo eliminar el directorio {locacion}: {e}")
        elif os.path.isfile(locacion):
            # Eliminar archivo
            try:
                nombre=os.path.basename(locacion)
                os.remove(locacion)
                self.arbol_directorios.remove_node(locacion)
                info_label = tk.Label(frame)
                info_label.config(text="La archivo '{}' fue eliminado".format(nombre))
            except OSError as e:
                print(f"No se pudo eliminar el archivo {locacion}: {e}")
        else:
            print(f"Ubicación inválida: {locacion}")