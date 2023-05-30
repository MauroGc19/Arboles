valores = {}
arr=[1, 2, 3, 4, 5, 6, 7]
k=14
contador=0
    # Recorrer el array
for num in arr:
    # Calcular el complemento de cada valor en el diccionario
    complemento = k - num
        
    # Si el complemento está en el diccionario, imprimir el par
    if complemento in valores:
        print(f"({num}, {complemento})")
        contador=1+contador   
    # Agregar el valor actual al diccionario
    valores[num] = True
if contador==0:
    print("no hay numeros pares que den el numero dado")
    
# En este algoritmo, se utiliza un diccionario para almacenar los valores del array a
# medida que se recorre. Para cada valor en el array, se calcula el complemento 
# necesario para sumar k. Si el complemento ya se encuentra en el diccionario, 
# se imprime el par de valores que suman k. De lo contrario, se agrega el valor 
# actual al diccionario y se continúa iterando sobre el array.

# Para usar este algoritmo, simplemente llama a la función encontrar_pares_suma(arr, k) 
# y pasa el array arr y el número objetivo k como argumentos. El algoritmo imprimirá
# todos los pares de elementos en el array que sumen k. Por ejemplo, para encontrar
# todos los pares de elementos en el array [1, 2, 3, 4, 5] que sumen 7, puedes
# llamar a la función así: encontrar_pares_suma([1, 2, 3, 4, 5], 7). 
# El resultado será (2, 5) y (3, 4).