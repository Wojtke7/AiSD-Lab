import math


class Circle:
    radius = 0
    area = 0

    def insert_data(self):
        self.radius = float(input("Type radius length: "))

    def calculate_area(self):
        print("Area is: ", math.pi * pow(self.radius, 2))

    def calculate_circumference(self):
        print("Circumference is: ", 2 * math.pi * self.radius)


class Triangle:
    sides = [0, 0, 0]
    p = 0

    def insert_data(self):
        correct = True
        while correct:
            for i in range(len(self.sides)):
                self.sides[i] = float(input("Type three sides of triangle: "))
            if self.sides[0] + self.sides[1] > self.sides[2] and self.sides[1] + self.sides[2] > self.sides[0] and self.sides[0] + self.sides[2] > self.sides[1]:
                self.p = sum(self.sides) / 2
                correct = False
            else:
                print("This is not a triangle, try again")

    def calculate_area(self):
        print("Area is: ", math.sqrt(self.p * (self.p - self.sides[0]) * (self.p - self.sides[1]) * (self.p - self.sides[2])))

    def calculate_circumference(self):
        print("Circumference is: ", sum(self.sides))


class Square:
    a = 0

    def __init__(self):
        self.a = float(input("Type square side: "))

    def calculate_area(self):
        print("Area is: ", pow(self.a, 2))

    def calculate_circumference(self):
        print("Circumference is: ", 4*self.a)
