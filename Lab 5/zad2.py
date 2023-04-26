import time


def moveIterative(sour, dest, a, b):
    #print(f"Disk, from {a}, to {b}")
    dest.append(min(sour))
    sour.pop()


def Hanoi(n, sour, dest, buff):
    i = 1
    sour_val = []
    for a in range(n):
        sour_val.append(n - a)
    dest_val = []
    buff_val = []

    while len(sour_val) != 0 or len(buff_val) != 0:
        if i % 3 == 1:
            if not dest_val or (dest_val and sour_val and min(sour_val) < min(dest_val)):
                moveIterative(sour_val, dest_val, sour, dest)
            else:
                moveIterative(dest_val, sour_val, dest, sour)
        if i % 3 == 2:
            if not buff_val or (buff_val and sour_val and min(sour_val) < min(buff_val)):
                moveIterative(sour_val, buff_val, sour, buff)
            else:
                moveIterative(buff_val, sour_val, buff, sour)
        if i % 3 == 0:
            if not dest_val or (dest_val and buff_val and min(buff_val) < min(dest_val)):
                moveIterative(buff_val, dest_val, buff, dest)
            else:
                moveIterative(dest_val, buff_val, dest, buff)
        i += 1
    return i - 1


start_time = time.time()
Hanoi(15, "A", "B", "C")
end_time = time.time()

sum = end_time - start_time

print(sum)
