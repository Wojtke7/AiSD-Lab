import time


def naive(list):
    places = []

    for i in range(0, len(list)):
        s = 0
        while (s + 2) < len(list[i]) and (i + 2) < len(list):
            if list[i][s] == 'A' and list[i][s + 1] == 'B' and list[i][s + 2] == 'C':
                if list[i + 1][s] == 'B' and list[i + 2][s] == 'C':
                    places.append({"y": i, "x": s})
            s += 1

    return places


class RollingHash:
    def __init__(self, word, word_size):
        self.text = word
        self.hash = 0
        self.sizeWord = word_size

        for i in range(0, word_size):
            self.hash += (ord(self.text[i]) - ord("a") + 1) * (26 ** (word_size - i - 1))

        self.window_start = 0
        self.window_end = word_size

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            self.hash -= (ord(self.text[self.window_start]) - ord("a") + 1) * 26 ** (self.sizeWord - 1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end]) - ord("a") + 1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return ''.join(self.text[self.window_start:self.window_end])


def rabin_karp_matcher(word, list):
    places = []

    for i in range(0, len(list) - 2):

        rolling_hash = RollingHash(list[i], len(word))
        key_word_hash = RollingHash(word, len(word))

        for j in range(len(list[i]) - len(word) + 1):
            if rolling_hash.hash == key_word_hash.hash:
                if rolling_hash.window_text() == word:
                    vertical = [list[i][j], list[i + 1][j], list[i + 2][j]]
                    letters = RollingHash(vertical, len(vertical))
                    if letters.hash == key_word_hash.hash:
                        if letters.window_text() == word:
                            places.append({"y": i, "x": j})
            rolling_hash.move_window()

    return places


with open('./patterns/1000_pattern.txt') as file:  # 1000_pattern
    lines = [line.split() for line in file]

list_of_1000 = []
for line in lines:
    for l in line:
        list_of_1000.append(list(l))

with open('./patterns/2000_pattern.txt') as file:  # 2000_pattern
    lines = [line.split() for line in file]

list_of_2000 = []
for line in lines:
    for l in line:
        list_of_2000.append(list(l))

with open('./patterns/3000_pattern.txt') as file:  # 3000_pattern
    lines = [line.split() for line in file]

arr_3000 = []
for line in lines:
    for l in line:
        arr_3000.append(list(l))

with open('./patterns/4000_pattern.txt') as file:  # 4000_pattern
    lines = [line.split() for line in file]

list_of_4000 = []
for line in lines:
    for l in line:
        list_of_4000.append(list(l))

with open('./patterns/5000_pattern.txt') as file:  # 5000_pattern
    lines = [line.split() for line in file]

list_of_5000 = []
for line in lines:
    for l in line:
        list_of_5000.append(list(l))

with open('./patterns/8000_pattern.txt') as file:  # 8000_pattern
    lines = [line.split() for line in file]

list_of_8000 = []
for line in lines:
    for l in line:
        list_of_8000.append(list(l))


def check_time(word, list):
    start_time = time.time()
    naive(list)
    end_time = time.time()
    print(f"{len(list)} pattern naive: {end_time - start_time}")
    start_time = time.time()
    print(f"Number of occurrences: {len(rabin_karp_matcher(word, list))}")
    end_time = time.time()
    print(f"{len(list)} pattern rabin karp: {end_time - start_time}")


check_time("ABC", list_of_1000)

check_time("ABC", list_of_2000)

check_time("ABC", list_of_4000)

check_time("ABC", list_of_5000)

check_time("ABC", list_of_8000)
