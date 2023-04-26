
import time
# sour = [1, 5, 9, 15, 20]
# dest = []
# buff = []

def disk_moving(n, sour, dest):
    #print(f"Disk {n}, from {sour} to {dest}")
    pass

def Hanoi(n, sour, dest, buff):
    if n == 1:
        #disk_moving(n, sour, dest)
        return
    Hanoi(n - 1, sour, buff, dest)
    #disk_moving(n, sour, dest)
    Hanoi(n - 1, buff, dest, sour)
    return


# Hanoi(5, sour, dest, buff)
# print(sour)
# print(dest)
start_time = time.time()
Hanoi(15, "A", "C", "B")
end_time = time.time()

sum = end_time - start_time

print(sum)
