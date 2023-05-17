
T = ['a', 'c', 'a', 'a', 'b', 'c']
P = ['a', 'a', 'b']


def naive_string_matcher(T, P):
    n = len(T)
    m = len(P)
    for s in range(0, n-m):
        counter = 0
        for i in range(m):
            if P[i] == T[s]:
                counter += 1
            else:
                break
            s += 1

        if counter == m:
            print(f"This pattern exist with {s-m} time shift")


naive_string_matcher(T, P)
