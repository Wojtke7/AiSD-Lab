import math
import random


def calc_sin(x):
    return math.sin(x)


def sin_formula(a, b, N):
    value = 0
    for i in range(N):
        j = random.uniform(a, b)
        value += calc_sin(j)
    print(value)
    return (b - a)/N * value


def circle_formula(N, radius):
    value = 0
    square = pow(2*radius, 2)
    for i in range(N):
        j = random.uniform(-radius, radius)
        z = random.uniform(-radius, radius)

        summary = math.hypot(j, z)
        if summary <= radius:
            value += 1

    return square * value / N


def second_circle_formula(a, b, N, radius):
    value = 0
    square = pow(2*radius, 2)
    for i in range(N):
        j = random.uniform(-radius, radius)
        z = random.uniform(-radius, radius)

        summary = math.hypot(j, z)
        if summary <= radius and a <= j <= b:
            value += 1

    return square * value / N


print("Tell me, in what limits you want to calculate tour integral of sin(x)")
accuracy = 100000
a_limit = float(input("From: "))
b_limit = float(input("To: "))

integral = sin_formula(a_limit, b_limit, accuracy)

print("Here is your integral: ", integral)
print("Insert circle radius, and limits")
c_limit = float(input("From: "))
d_limit = float(input("To: "))
circle_radius = float(input("Radius: "))

integral2 = circle_formula(accuracy, circle_radius)
integral3 = second_circle_formula(c_limit, d_limit, accuracy, circle_radius)

print("Here is your circle integral: ", integral2)
print("EO: ", integral3)
