import time

length = 100000

lista1 = [i for i in range(length)]

start_time = time.time()

suma = 0

for i in lista1:
    suma += i

print(suma)
print("Czas:", (time.time() - start_time))

suma = 0 

for i in range(length):
    suma += lista1[i]

print(suma)
print("Czas:", (time.time() - start_time))