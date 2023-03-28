
numbers = []

for i in range(500,3001):
    if i %7 == 0 and i %5 != 0:
        numbers.append(i)

string = ''.join(str(i) for i in numbers)
#print(string)

counter = string.count('21')
string = string.replace('21','XX')

print(string)
print(counter)