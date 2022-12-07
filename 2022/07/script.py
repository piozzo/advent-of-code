########################################
# --- Day 7: No Space Left On Device ---
########################################
import sys
import re

class Node:
	def __init__(self, data):
		self.childs = []
		self.data = data
		self.father = None

	def __str__(self):
		s = f"{self.data[0]}, size: {self.size()}, sizePart1: {self.sizePart1()} name: {self.fullName()}\n"
		for c in self.childs:
			s += str(c)
		return s

	def name(self):
		return self.data[2]

	def size(self):
		return self.data[1] + sum([x.size() for x in self.childs])

	def sizePart1(self):
		return self.size() if self.data[0] == "d" and self.size() <= 100000 else 0

	def sizePart2(self):
		return self.size() if self.data[0] == "d" and self.size() >= freeSpaceRequired else 0

	def fullName(self):
		if self.father is None:
			return "";
		return self.father.fullName() + "/" + self.data[2]

def addNode(node, data):
	n = Node(data)
	n.father = node
	node.childs.append(n)

def getChildNode(n, name):
	for cn in n.childs:
		if cn.data[2] == name:
			return cn

def sizePart1(node):
	return node.sizePart1() + sum([sizePart1(x) for x in node.childs])

def sizePart2(node):
	nodes = []

	dim = node.sizePart2()
	if (dim > 0):
		nodes.append(dim)

	for c in node.childs:
		nodes += sizePart2(c)

	nodes = list(set(nodes))
	return nodes

fs = Node(("d", 0, "/"))
currentNode = fs

diskSpaceAvailable = 70000000
updateSize = 30000000
input = sys.stdin.read().strip().split("\n")
inputLines = len(input)

i = 1
while (i<inputLines):
	if re.match("^\\$ cd", input[i]):
		dest = input[i].split(" ")[2]
		if dest == "..":
			currentNode = currentNode.father
		else:
			currentNode = getChildNode(currentNode, dest)
		i+=1
	elif input[i] == "$ ls":
		i+=1
		while (i<inputLines and not re.match("^\\$", input[i])):
			if re.match("^\d+", input[i]):
				p = input[i].split(" ")
				addNode(currentNode, ("f", int(p[0]), p[1]))
			else:
				addNode(currentNode, ("d", 0, input[i].split(" ")[1]))
			i+=1

fsSize = fs.size()
freeSpace = diskSpaceAvailable - fsSize
freeSpaceRequired = updateSize - freeSpace

print("Total part1: " + str(sizePart1(fs)))
print("Total part2: " + str(min(sizePart2(fs))))
