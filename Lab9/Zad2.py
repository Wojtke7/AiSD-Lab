import random
import time
import numpy as np
import multiprocessing

BACKPACK_SIZE = 20

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

    def get_value(self):
        return self.value


class Item:
    def __init__(self, _id, width, height, value):
        self._id = _id
        self.width = int(width)
        self.height = int(height)
        self.value = int(value)

    def copy(self):
        copied_item = Item(self._id, self.width, self.height, self.value)
        return copied_item


with open("packages/packages100.txt", 'r') as file:
    for line in file:
        line = line.strip().split('\n')
        items_specs.append(line[0].split(','))
        # print(line)

items_specs.pop(0)
items_specs.pop(0)
items = []

for cord in items_specs:
    items.append(Item(cord[0], cord[1], cord[2], cord[3]))


def eval(gene):
    if isinstance(gene[-1], int):
        return 0
    backpack = Backpack(BACKPACK_SIZE, BACKPACK_SIZE)
    for item in gene:
        backpack.add_item(item)
    return backpack.get_value()


def ant_algorithm():
    p = 100  # population size
    pc = 0.2  # elite percentage
    pm = 0.01  # mutations
    ps = 0.05  # mutation severity

    population = []
    try:
        counter = 0
        while counter < 300:
            counter += 1
            # generate random population
            for i in range(p - len(population)):
                population.append(random.sample(items, k=len(items)))

            # print(population)
            # multicore eval
            pool = multiprocessing.Pool()
            result = pool.map(eval, population)
            # print(result)

            for i in range(len(population)):
                if not isinstance(population[i][-1], int):
                    population[i].append(result[i])

            # uncomment to get single core eval
            # # eval genes
            # for gene in population:
            #     if not isinstance(gene[-1], int):
            #         gene.append(eval(gene))

            # sort according to perceived value
            population.sort(key=lambda g: -g[-1])
            print(counter, population[0][-1])

            # breed
            for i in range(round(p - 2 * pc * p)):
                b = random.randint(0, pc * p - 1)
                c = random.randint(pc * p, p - 2)
                bc = []
                iter_b = 0
                iter_c = 0
                for j in range(len(items)):
                    # randomize gene mixing
                    mixer = random.randint(0, 1)
                    if mixer:
                        while population[b][iter_b] in bc:
                            iter_b += 1

                        if iter_b <= len(items):
                            bc.append(population[b][iter_b].copy())
                        else:
                            bc.append(population[c][iter_c].copy())

                    else:
                        while population[c][iter_c] in bc:
                            iter_c += 1

                        if iter_c <= len(items):
                            bc.append(population[c][iter_c].copy())
                        else:
                            bc.append(population[b][iter_b].copy())

                population.append(bc)
                # population[-1].append(eval(population[-1]))

            del population[round(pc * p):p]

            # mutate
            for i in range(round(pm * len(population))):
                # pick entity to mutate
                m = random.randint(0, len(population) - 1)
                for j in range(round(ps * len(items))):
                    # pick two genes to swap
                    m1 = random.randint(0, len(items) - 1)
                    m2 = random.randint(0, len(items) - 1)

                    temp = population[m][m1].copy()
                    population[m][m1] = population[m][m2].copy()
                    population[m][m2] = temp
                    if isinstance(population[m][-1], int):
                        del population[m][-1]
                    # eval new genome
                    # population[m].append(eval(population[m]))
        print(counter, population[0][-1])

    except KeyboardInterrupt:
        pass
        # print(population[0])
        # print(len(population[0]))
        # print(len(population))


start_time = time.time()
ant_algorithm()
end_time = time.time()
print(f"Total time: {end_time - start_time}")
