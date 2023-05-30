import numpy
array=[1, 2, 3, 5,2234,23425,235,12,2,3,3,45,9]
# def suma(array):
#     suma=0
#     for elem in numpy.size(array) :
#         if array[elem+1]:
#             if suma <array[elem]+array[elem+1]:
#                 suma = array[elem]+array[elem+1]
#     return suma
# print(suma(array))

# array.sort()
# numero1=array[-1] 
# numero2=array[-2]
# print(numero1)
# print(numero2)
# print(numero1+numero2)
# total = array.count()
# print(total)
i=0
for n in array:
    if n > i:
        i=n
    max=i
l=0
for n in array:
    if n > l and n != max:
        l=n
    max2=l

print(max)
print(max2)

 

         