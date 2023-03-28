file = open('Lab2/zadanie2.csv', 'r')     
        
txt = file.read()

txt = txt.splitlines()
txt = [l.split(',') for l in txt]

file.close()

for line in txt:
    if line[1] == '':
        line.pop(1)
        line.pop(0)    

txt2 = []

for line in txt:
    if line != []:
        txt2.append(line)



print("###")
txt2.sort()

for line in txt2:
    for i in range(len(line)):
        line[i] = line[i].lower()


print(txt2)
