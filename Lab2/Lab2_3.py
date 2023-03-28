import time

f= open('Lab2/SJP.txt', 'r')

txt = f.read()

text = input("Type something: ")

if text.count(" ") > 0:
    if text.isspace():
        print("Empty text")
    else:
        print("Some words")
else:
    print("One word")
    text = text.lower()
    stime = time.time()
    if text in txt:
        print("It's polish word")
    else:
        print("It's not polish word")


print("Execution time: ", time.time() - stime)