a = '1'
b = 2
try:
    c = a + b
except TypeError:
    print("Wrong variable type!")
    c = 0

x = 3
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Division error!")

list = [0] * 50

try:
    print(lista[2])
except NameError:
    print("Wrong name!")