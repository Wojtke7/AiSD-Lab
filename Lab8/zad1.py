import math
import time

def distance(x1, x2, y1, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


with open("TSP.txt", "r") as file:
    towns = [line.split() for line in file]

towns = [[float(x) for x in town] for town in towns]

curr_distance = 0

for i in range(len(towns)):

    if i != len(towns) - 1:
        curr_distance += distance(towns[i][1], towns[i + 1][1], towns[i][2], towns[i + 1][2])
    else:
        curr_distance += distance(towns[i][1], towns[0][1], towns[i][2], towns[0][2])

print(curr_distance)


def nearest_path(list_of_towns):
    global town_to_delete

    global_distance = 0

    while list_of_towns:
        dist = 0

        for town in list_of_towns:
            rest_of_towns = list_of_towns[1:]
            for i in range(len(rest_of_towns)):
                new_dist = distance(town[1], rest_of_towns[i][1], town[2], rest_of_towns[i][2])
                if new_dist < dist or dist == 0:
                    town_to_delete = town
                    dist = new_dist

            global_distance += dist
            if not rest_of_towns:
                break
            index = list_of_towns.index(town_to_delete)
            list_of_towns.pop(index)

        if len(list_of_towns) == 1:
            break

    return global_distance

start_time = time.time()
print(nearest_path(towns))
end_time = time.time()

print(f"Time: {end_time - start_time}")
