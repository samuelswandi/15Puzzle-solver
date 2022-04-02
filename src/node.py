# Importing the heap functions from python
# library for Priority Queue
from heapq import heappush, heappop

class priorityQueue:
     
    # Constructor to initialize a
    # Priority Queue
    def __init__(self):
        self.heap = []
 
    # Inserts a new key 'k'
    def push(self, k):
        heappush(self.heap, k)
 
    # Method to remove minimum element
    # from Priority Queue
    def pop(self):
        return heappop(self.heap)
 
    # Method to know if the Queue is empty
    def empty(self):
        if not self.heap:
            return True
        else:
            return False
 
# Node structure
class node:
     
    def __init__(self, parent, mat, cost, depth, command):
                      
        # Stores the parent node of the
        # current node helps in tracing
        # path when the answer is found
        self.parent = parent
 
        # Stores the matrix
        self.mat = mat
 
        # Stores the number of misplaced tiles
        self.cost = cost 
 
        # Stores the number of depth so far
        self.depth = depth

        # Stores the command used for this node
        self.command = command
 
    # This method is defined so that the
    # priority queue is formed based on
    # the cost variable of the objects
    def __lt__(self, nxt):
        if self.cost + self.depth == nxt.cost + nxt.depth:
            return self.cost < nxt.cost
        return self.cost + self.depth < nxt.cost + nxt.depth