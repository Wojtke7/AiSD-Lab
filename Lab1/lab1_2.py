import time
import statistics
from array import *

def unique_list(lista1):
    
    lista2 = [] 
    for i in lista:
        if i not in lista2:
            lista2.append(i)

    return lista2

start_time = time.time()

lenght = 48
lista = array('f',[0 for i in range(lenght)])

lista[0] = 1
lista[1] = 2 

for i in range (2,lenght):
    lista[i] = (lista[(i-1)] + lista[(i-2)])/(lista[(i-1)] - lista[(i-2)])

print(lista)

suma = 0

for i in lista:
    suma += i

print("Średnia: " , suma/lenght)
print("Moda: ", statistics.mode(lista))

counter = 0
unikalna_lista = unique_list(lista)

for i in unikalna_lista:
    counter = 0
    for l in lista:
        if i == l:
            counter += 1
    if counter > 1:
        print("Element", i, "występuje", counter, "razy")
    else:
        print("Element", i, "jest unikalny")

print(time.time() - start_time)
             