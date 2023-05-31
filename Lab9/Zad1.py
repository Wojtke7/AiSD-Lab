import time

import numpy as np

items_specs = []


class Backpack:
    def __init__(self, height, width):
        self.width = int(width)
        self.height = int(height)
        self.field = np.zeros((self.width, self.height))
        self.items = []
        self.value = 0

    def add_item(self, item):
        item_width, item_height = item.height, item.width
        for w in range(self.width - item_width + 1):
            if w + item_width > self.width + 1:
                break
            for h in range(self.height - item_height + 1):
                if h + item_height > self.height + 1:
                    break
                if np.all(self.field[w: w + item_width, h: h + item_height] == 0):
                    self.field[w: w + item_width, h: h + item_height] = item._id
                    self.value += item.value
                    return True
        # rotation
        item_width, item_height = item_height, item_width
        for w in range(self.width - item_width + 1):
            if w + item_width > self.width:
                break
            for h in range(self.height - item_height + 1):
                if h + item_height > self.height + 1:
                    break
                if np.all(self.field[w: w + item_width, h: h + item_height] == 0):
                    self.field[w: w + item_width, h: h + item_height] = item._id
                    self.value += item.value
                    return True
        return False

    def display_backpack(self):
        print(self.field)

    def get_value_of_items(self):
        return self.value


class Item:
    def __init__(self, _id, width, height, value):
        self._id = _id
        self.width = int(width)
        self.height = int(height)
        self.value = int(value)


def greedy_algorithm(backpack, items):
    temp_items = items
    temp_items.sort(key=lambda item: item.value/(item.height * item.width), reverse=True)
    for item in temp_items:
        backpack.add_item(item)


with open("packages/packages100.txt", 'r') as file:
    for line in file:
        line = line.strip().split('\n')
        items_specs.append(line[0].split(','))
        #print(line)

items_specs.pop(0)
items_specs.pop(0)
items = []

#print(items_specs)
for cord in items_specs:
    items.append(Item(cord[0], cord[1], cord[2], cord[3]))

backpack1 = Backpack(20, 20)

start_time = time.time()
greedy_algorithm(backpack1, items)
end_time = time.time()
print(f"Total time: {end_time - start_time}")
print(f"Value of greedy algorithm: {backpack1.get_value_of_items()}")
backpack1.display_backpack()
