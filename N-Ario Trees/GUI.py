import tkinter as tk
from tkinter import filedialog, simpledialog
from proyecto1 import *

class GUI:
    def __init__(self, gestor):
        self.gestor = gestor
        
        self.root = tk.Tk()
        self.root.title("Gestor de Archivos")
        # Obtener el ancho y alto de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (screen_width - 400) // 2  # Centrar horizontalmente con un ancho de 400 píxeles
        y = (screen_height - 300) // 2  # Centrar verticalmente con un alto de 300 píxeles

        # Establecer la posición de la ventana en el centro de la pantalla
        self.root.geometry(f"400x300+{x}+{y}")
        
        info_label = tk.Label(self.root, text="Instrucciones de uso: 1. primero con la funcion explorar eliges la carpeta donde quieres ver sus archivos)")
        info_label.pack()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.BOTTOM)
        
        self.explorar_button = tk.Button(self.frame, text="Explorar", command=self.explorar)
        self.explorar_button.pack(side=tk.LEFT)
        
        self.renombrar_button = tk.Button(self.frame, text="Renombrar", command=self.renombrar)
        self.renombrar_button.pack(side=tk.LEFT)
        
        self.eliminar_button = tk.Button(self.frame, text="Eliminar", command=self.eliminar)
        self.eliminar_button.pack(side=tk.LEFT)
        
    def explorar(self):
        ruta_inicial = filedialog.askdirectory(title="Seleccionar directorio")
        self.gestor.arbol_directorios.add_node(ruta_inicial)
        frame=tk.Frame(self.root)
        frame.pack()
        if ruta_inicial:
            self.gestor.explorar(ruta_inicial,frame, ruta_inicial)
    
    def renombrar(self):
        info_label = tk.Label(self.root)
        info_label.pack()
        ruta_original = filedialog.askdirectory(title="Seleccionar directorio original")
        nuevo_nombre = simpledialog.askstring("Nuevo nombre", "Ingrese el nuevo nombre:") 
        self.gestor.renombrar(ruta_original, nuevo_nombre,info_label)
    
    def eliminar(self):
        frame=tk.Frame(self.root)
        frame.pack()
        locacion = filedialog.askdirectory(title="Seleccionar directorio o archivo para eliminar")
        if locacion:
            self.gestor.eliminar(locacion, frame)
    
    def run(self):
        self.root.mainloop()

# # Crear una instancia de la clase Gestor
# gestor = Gestor()

# # Crear una instancia de la clase GUI pasando el gestor como argumento
# gui = GUI(gestor)

# # Ejecutar la interfaz gráfica
# gui.run()
