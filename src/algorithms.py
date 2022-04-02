import source
import time
import node

def copyNodeMatrixFrom(matrix):
    copy = [[]]
    for i in range(4):
        copy.append([])
        for j in range(4):
            copy[i].append(matrix[i][j])
    return copy


def calculateCostOf(node):
    totalCost = 0
    count = 1
    for i in range(4):
        for j in range(4):
            if node[i][j] != 16:
                if node[i][j] != count:
                    totalCost += 1
            count += 1

    return totalCost

def theSameWith(initialNode, customizedNode):
    for i in range(4):
        for j in range(4):
            if initialNode[i][j] != customizedNode[i][j]:
                return False
    return True

def theSameWithTheRestOf(visitedNodes, nodes):
    for i in visitedNodes:
        if theSameWith(i.mat, nodes):
            return True
    return False

# change current Node to the next Node where the it chose UP command
def up(Node):
    found = False
    for i in range(4):
        for j in range(4):
            if Node[i][j] == 16 and i != 0 and not found:
                Node[i][j], Node[i-1][j] = Node[i-1][j], Node[i][j]
                found = True
    return Node

# change current Node to the next Node where the it chose DOWN command
def down(Node):
    found = False
    for i in range(4):
        for j in range(4):
            if Node[i][j] == 16 and i != 3 and not found:
                Node[i][j], Node[i+1][j] = Node[i+1][j], Node[i][j]
                found = True
    return Node

# change current Node to the next Node where the it chose LEFT command
def left(Node):
    found = False
    for i in range(4):
        for j in range(4):
            if Node[i][j] == 16 and j != 0 and not found:
                Node[i][j-1], Node[i][j] = Node[i][j], Node[i][j-1]
                found = True
    return Node

# change current Node to the next Node where the it chose RIGHT command
def right(Node):
    found = False
    for i in range(4):
        for j in range(4):
            if Node[i][j] == 16 and j != 3 and not found:
                Node[i][j+1], Node[i][j] = Node[i][j], Node[i][j+1]
                found = True
    return Node

# to generate node from the current Node
# to choose node with the lowest cost
def generateNodeFrom(visitedNodes, parent):
    listOfNodes = []
    listOfCommand = ["right", "left", "down", "up"]
    for i in listOfCommand:
        
        # to have a copy of Node
        # because if we use Node, python will change the value of Node itself
        # (python use reference instead of copy value lol)
        copyOfNodeMatrix = copyNodeMatrixFrom(parent.mat)

        # just a bunch of code to generate node from the current Node
        if i == "up":
            upNodeMatrix = up(copyOfNodeMatrix)
            if not theSameWithTheRestOf(visitedNodes, upNodeMatrix):
                newNode = node.node(parent, upNodeMatrix, calculateCostOf(upNodeMatrix), parent.depth+1, i)
                listOfNodes.append(newNode)

        if i == "down":
            downNodeMatrix = down(copyOfNodeMatrix)
            if not theSameWithTheRestOf(visitedNodes, downNodeMatrix):
                newNode = node.node(parent, downNodeMatrix, calculateCostOf(downNodeMatrix), parent.depth+1, i)
                listOfNodes.append(newNode)
                
        if i == "left":
            leftNodeMatrix = left(copyOfNodeMatrix)
            if not theSameWithTheRestOf(visitedNodes, leftNodeMatrix):
                newNode = node.node(parent, leftNodeMatrix, calculateCostOf(leftNodeMatrix), parent.depth+1, i)
                listOfNodes.append(newNode)

        if i == "right":
            rightNodeMatrix = right(copyOfNodeMatrix)
            if not theSameWithTheRestOf(visitedNodes, rightNodeMatrix):
                newNode = node.node(parent, rightNodeMatrix, calculateCostOf(rightNodeMatrix), parent.depth+1, i)
                listOfNodes.append(newNode)

    return listOfNodes


def solver(parent):

    # IF THE FIRST PUZZLE IS ALREADY SOLVED LOL
    if calculateCostOf(parent.mat) == 0:
        source.printPuzzleInNode(parent)
        print("YOU PUZZLE HAS ALREADY BEEN SOLVED!")
        return [parent.mat]

    # add parent to visited nodes
    visitedNodes = [parent] 

    # generate node from the current parent
    listOfNodes = generateNodeFrom(visitedNodes, parent)

    # push to prio queue
    pq = node.priorityQueue()
    for i in listOfNodes:
        pq.push(i)

    countVisitedNodes = 0
    while not pq.empty():
        nodes = pq.pop()
        visitedNodes.append(nodes)
        countVisitedNodes+=1
        
        print(f"====== {countVisitedNodes} ======")
        print(f"Move {nodes.command} is chosen")
        source.printPuzzleInNode(nodes)

        if calculateCostOf(nodes.mat) == 0:
            print("YOU PUZZLE HAS BEEN SOLVED!")
            return visitedNodes
        listOfNodes = generateNodeFrom(visitedNodes, nodes)
        for i in listOfNodes:
            pq.push(i)

