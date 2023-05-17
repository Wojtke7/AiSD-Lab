import numpy as np
import random
import time


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class NodeList:
    def __init__(self):
        self.list = []


class BinTree:
    def __init__(self):
        self.nodeList = NodeList()

    def insertNode(self, value):
        for i in self.nodeList.list:
            if i.value == value:
                break
            elif i.value > value:
                self.nodeList.list.insert(self.nodeList.list.index(i), Node(value))
                break
        else:
            self.nodeList.list.append(Node(value))

    def insertValue(self, value):
        for index, node in enumerate(self.nodeList.list):
            if abs(node.value - value) <= 0.5 and node.value != value:
                if index + 1 < len(self.nodeList.list) and abs(self.nodeList.list[index + 1].value - value) <= 0.5:
                    current_node = self.nodeList.list[index + 1]
                    self.insertValueInChild(current_node, value)
                    break
                else:
                    current_node = self.nodeList.list[index]
                    self.insertValueInChild(current_node, value)
                    break

    def insertValueInChild(self, node, value):
        if value < node.value:
            if node.left_child is None:
                node.left_child = Node(value)
            else:
                self.insertValueInChild(node.left_child, value)
        elif value > node.value:
            if node.right_child is None:
                node.right_child = Node(value)
            else:
                self.insertValueInChild(node.right_child, value)

    def print(self):
        for i in self.nodeList.list:
            self.printTree(i)
            print("")
        print("")

    def printTree(self, node, indent=0):
        if node is not None:
            print(' ' * indent + str(node.value), end="")
            self.printChildren(node.left_child, indent + 4)
            self.printChildren(node.right_child, indent + 4)

    def printChildren(self, node, indent, count=1):
        if node is not None:
            print("\n" + ' ' * indent + "-" * count, end="")
            print(str(node.value), end="")
            self.printChildren(node.left_child, indent + 4, count + 1)
            self.printChildren(node.right_child, indent + 4, count + 1)

    def minimum(self, nodeValue):
        node = None
        for i in self.nodeList.list:
            if i.value == nodeValue:
                node = i
                break
        if node is None:
            return None
        elif node.left_child is None:
            return node.value
        else:
            return self._minimum(node.left_child)

    def _minimum(self, node):
        if node.left_child is None:
            return node.value
        else:
            self._minimum(node.left_child)

    def maximum(self, nodeValue):
        node = None
        for i in self.nodeList.list:
            if i.value == nodeValue:
                node = i
                break
        if node is None:
            return None
        elif node.right_child is None:
            return node.value
        else:
            return self._maximum(node.right_child)

    def _maximum(self, node):
        if node.right_child is None:
            return node.value
        else:
            return self._maximum(node.right_child)

    def search(self, value):
        current_node = None
        for index, node in enumerate(self.nodeList.list):
            if node.value == value:
                return True
            elif abs(node.value - value) <= 0.5:
                if index + 1 < len(self.nodeList.list) and abs(self.nodeList.list[index + 1].value - value) <= 0.5:
                    current_node = self.nodeList.list[index + 1]
                    break
                else:
                    current_node = self.nodeList.list[index]
                    break
        while current_node is not None:
            if current_node.value == value:
                return True
            elif value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False


def insertTime(tree, iterations=10):
    result_list = []
    for i in range(iterations):
        index = random.randint(0, len(tree.nodeList.list) - 1)
        currentNode = tree.nodeList.list[index]
        value = round(random.uniform(currentNode.value - 0.5, currentNode.value + 0.49), 2)
        start = time.time()
        tree.insertValue(value)
        end = time.time()
        result_list.append(end - start)
    return np.mean(result_list)


def minTime(tree, count=10):
    result = []
    for i in range(count):
        index = random.randint(0, len(tree.nodeList.list) - 1)
        start = time.time()
        tree.minimum(tree.nodeList.list[index].value)
        end = time.time()
        result.append(end - start)
    return np.mean(result)


def maxTime(tree, count=10):
    result = []
    for i in range(count):
        index = random.randint(0, len(tree.nodeList.list) - 1)
        start = time.time()
        tree.maximum(tree.nodeList.list[index].value)
        end = time.time()
        result.append(end - start)
    return np.mean(result)


def searchTime(tree, count=10):
    result = []
    for i in range(count):
        index = random.randint(0, len(tree.nodeList.list) - 1)
        currentNode = tree.nodeList.list[index]
        value = round(random.uniform(currentNode.value - 0.5, currentNode.value + 0.49), 2)
        start = time.time()
        tree.search(value)
        end = time.time()
        result.append(end - start)
    return np.mean(result)


def task1(tree):
    tree.insertNode(1.5)
    tree.insertNode(3.5)
    tree.insertNode(4.5)
    tree.insertNode(7.5)
    tree.insertNode(9.5)
    tree.insertValue(1.3)
    tree.insertValue(1.6)
    tree.insertValue(3.7)
    tree.insertValue(4.0)
    tree.insertValue(4.99)
    tree.insertValue(7.3)
    tree.insertValue(7.8)
    tree.insertValue(7.7)
    tree.insertValue(7.9)
    tree.insertValue(7.6)
    tree.insertValue(9.3)


def task2(tree):
    task1(tree)
    tree.insertNode(2.5)
    tree.insertNode(9.5)
    tree.insertValue(5)
    tree.insertValue(6.6)
    tree.insertValue(9.7)
    min = tree.minimum(5.5)
    max = tree.maximum(5.5)
    print(min)
    print(max)
    print(tree.search(6.5))


def task3(tree):
    elements = 1000
    iterations = 30
    nodes_amount = int(elements / 100)
    numbers = np.arange(0, 10000, 1)
    nodesValues = np.random.choice(numbers, nodes_amount) + 0.5
    for i in nodesValues:
        tree.insertNode(i)

    for i in range(elements - nodes_amount):
        index = random.randint(0, len(tree.nodeList.list) - 1)
        currentNode = tree.nodeList.list[index]
        value = round(random.uniform(currentNode.value - 0.5, currentNode.value + 0.49), 2)
        if tree.search(value):
            i -= 1
        else:
            tree.insertValue(value)

    print(f"Insertion for {elements} elements: {insertTime(tree, iterations)}")
    print(f"Min time for {elements} elements: {minTime(tree, iterations)}")
    print(f"Max time for {elements} elements: {maxTime(tree, iterations)}")
    print(f"Search time for {elements} elements: {searchTime(tree, iterations)}")


data = BinTree()
task1(data)
# task2(data)
task3(data)

data.print()
