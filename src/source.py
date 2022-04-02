import algorithms
import time
import node

def printIntro():
    print(""" 
░░███╗░░███████╗░░░░░░██████╗░██╗░░░██╗███████╗███████╗██╗░░░░░███████╗
░████║░░██╔════╝░░░░░░██╔══██╗██║░░░██║╚════██║╚════██║██║░░░░░██╔════╝
██╔██║░░██████╗░█████╗██████╔╝██║░░░██║░░███╔═╝░░███╔═╝██║░░░░░█████╗░░
╚═╝██║░░╚════██╗╚════╝██╔═══╝░██║░░░██║██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░
███████╗██████╔╝░░░░░░██║░░░░░╚██████╔╝███████╗███████╗███████╗███████╗
╚══════╝╚═════╝░░░░░░░╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝╚══════╝╚══════╝

            ░██████╗░█████╗░██╗░░░░░██╗░░░██╗███████╗██████╗░
            ██╔════╝██╔══██╗██║░░░░░██║░░░██║██╔════╝██╔══██╗
            ╚█████╗░██║░░██║██║░░░░░╚██╗░██╔╝█████╗░░██████╔╝
            ░╚═══██╗██║░░██║██║░░░░░░╚████╔╝░██╔══╝░░██╔══██╗
            ██████╔╝╚█████╔╝███████╗░░╚██╔╝░░███████╗██║░░██║
            ╚═════╝░░╚════╝░╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    """)


def isPuzzleSolvable(puzzle):
    totalSigma = 0
    x = 0
    # looping though the puzzle
    for i in range(4):
        for j in range(4):
            # mengecek tempat sel kosong. Apakah sel kosong berada pada sel yang diarsir
            if (puzzle[i][j] == 16):
                if (i % 2 == 0 and j % 2 != 0):
                    x = 1
                elif (i % 2 != 0 and j % 2 == 0):
                    x = 1

            # looping through current position until the end to check
            # whether there is number less than current number in current position
            total = 0
            for k in range(i,4):
                if k == i:
                    for l in range(j,4):
                        if puzzle[k][l] < puzzle[i][j]:
                            total += 1
                else:
                    for l in range(4):
                        if puzzle[i][j] > puzzle[k][l]:
                            total += 1

            print(f"Kurang[" , end="")
            if (puzzle[i][j] < 10):
                print("0", end="")
            print(puzzle[i][j], end="")
            print(f"] = {total}")
            totalSigma += total
            
    print(f"Total sigma + x: {totalSigma} + {x} = {totalSigma+x} ")
    return totalSigma + x

def printPuzzle(puzzle):
    for i in range(4):
        print("[ ", end="")
        for j in range(4):
            if (puzzle[i][j] == 16):
                print(" - " , end="")
            else:
                if (puzzle[i][j] < 10):
                    print(" ", end="")
                print(puzzle[i][j], end=" ")
        print("]")
    print()

def printPuzzleInNode(node):
    for i in range(4):
        print("[ ", end="")
        for j in range(4):
            if (node.mat[i][j] == 16):
                print(" - " , end="")
            else:
                if (node.mat[i][j] < 10):
                    print(" ", end="")
                print(node.mat[i][j], end=" ")
        print("]")
    print()

def readFromFile(filename):
    with open(filename, 'r') as f:
        puzzle = [[int(num) for num in line.split(' ')] for line in f]
        return puzzle


def mainProgram():
    # print intro hehe :D 
    printIntro()

    initialPuzzle = []

    print("Please choose how you want to input your puzzle:")
    choice = int(input("\n1. Read from file\n2. Input manually\n\nchoice: "))
    if (choice == 1):
        # input file to determine puzzle
        filename = input("Please input filename for puzzle: ")
        initialPuzzle = readFromFile("../test/" +filename)
    elif (choice == 2):
        initialPuzzle = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        print("Input the puzzle:")
        for i in range(4):
            for j in range(4):
                initialPuzzle[i][j] = int(input(f"puzzle[{i}][{j}] = "))
    else:
        print("Invalid input")
        return

    print("This is your initial puzzle: ")
    printPuzzle(initialPuzzle)
    
    # check whether the puzzle is solveable or not
    sigma = isPuzzleSolvable(initialPuzzle)
    
    # verdict of whether the puzzle is solveable or not
    print()
    print("Verdict: ")

    # if sigma is odd, then puzzle cannot be solved
    if sigma % 2 != 0:
        print("Your puzzle cannot be solved!")
        return
    else:
        start_time = time.time()
        print("Your puzzle can be solved!")
        print()
        # make initial Node 
        initialNode = node.node(initialPuzzle, initialPuzzle, sigma, 0, "-")
        visitedNodes = algorithms.solver(initialNode)
        print()
        print(f"The number of nodes visited: {len(visitedNodes)}")
        print()
        print("Total time of program execution:", time.time() - start_time)
