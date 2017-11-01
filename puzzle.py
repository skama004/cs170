import sys
import copy

goalPuzzleVec = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] 


class node:
	#create node class to expand tree for puzzle states
	#pymbooks.readthedocs.io/en/latest/classes.html
	heuristic = 0;
	depth = 0;
	#	self.puzzleAt = puzzleAt[0][0];
	
	def printPuzzle(self):
		print ''
		print self.puzzleAt[0][0], self.puzzleAt[0][1], self.puzzleAt[0][2]
		print self.puzzleAt[1][0], self.puzzleAt[1][1], self.puzzleAt[1][2]
		print self.puzzleAt[2][0], self.puzzleAt[2][1], self.puzzleAt[2][2]
	
	def initialize(self):
		self.heuristic = 0;
		self.depth = 0;
	

def main():
	print "Welcome to Siddaardha's 8-puzzle Solver! \n" 
	input = puzzleChoice() #what puzzle should we solve
	algorithm = algorithmChoice() #what algorithm should we choose to solve it
	solve = (input, algorithm)
		
	
def algorithmChoice():
	#Function to pick which of the three algorithms to use


def puzzleChoice():
	#Function created to choose what puzzle board user wants
	#Default
	#Enter your own puzzle (by row? )
	#Random puzzle
	#Quit	
	goalPuzzle = []
	startPuzzle = [] 
	defaultPuzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
	
	
	while 1:
		pickapuzzle = raw_input("Pick what puzzle you would like: 1 for default, 2 to build your own, 3 for random, 4 to quit\n")
		
		if(pickapuzzle == "1")
			print "Default puzzle chosen \n"
			startPuzzle = defaultPuzzle; 
			return startPuzzle
			
		elif(pickapuzzle == "2")
			print "DIY puzzle chosen. Use 0 to identify blank tile \n"
			firstrow = raw_input("Enter first 3 numbers for first row separated by spaces")
			
		elif(pickapuzzle == "3")
		
		elif(pickapuzzle == "4")
		
		
	
	
	#function to move tiles
def moveTile(puzzleChoice):	
	nodeslist = []
		
		
	#docs.python.org/2/library/copy.html
	#deep copy the puzzle into each variable so we can make changes depending on what moves we want to make
	#deep copy inserts the copies of objects into new object
	#regular shallow copy just copies the references to the objects 
		
	moveleft = copy.deepcopy(puzzleChoice)
	moveright = copy.deepcopy(puzzleChoice)
	moveup = copy.deepcopy(puzzleChoice)
	movedown = copy.deepcopy(puzzleChoice)
		
		
	for i in moveleft:
		if(i.count(' ') == 1):
			#if space is found 
				
	for i in moveright:
	for i in moveup:
	for i in movedown:
			
		
	return nodesList;
		
		
	
	
	#1. Uniform Cost Search
def uniformcost(puzzle):
	#g(n) = depth of a solution
	#h(n) = heuristic
	#root node push onto queue, pop it off and then expand, queue holds everything yet to be expanded
	#breadth first search
	
	#2. A* w/ Misplaced Tile Heuristic
def misplacedTile(puzzle):
	#use uniform cost search
	#how many that aren't in the right place
	#1, 2, 3, 4, 0, 6, 7, 5, 8
	#h(n) = 2 if misplaced from optimal (example Calvin showed you)
	#g(n) + h(n) = solution 
	#calculate g(n) and h(n) per node
	#put solution in a priority queue
	#sort with the solution value (g(n) + h(n) )



	#3. A* w/ Manhattan Distance Heuristic
def manhattanDist(puzzle):
	#instead of calculating tiles, calculate distance between correct tiles
