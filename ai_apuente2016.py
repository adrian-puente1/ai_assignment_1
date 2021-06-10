# CAP 4630 Intro to AI
# Assignment 1
# 06/10/2021
# Adrian Puente, Meike Buettner, Mohammad Khan

DESTINATION='BUCHAREST'
city_paths = {
    'ARAD':             [['ZERIND', 75], ['TIMISOARA', 118], ['SIBIU', 140]],
	'BUCHAREST':        [['URZICENI', 85], ['GIURGIU', 90], ['PITESTI', 101], ['FAGARAS', 211]],
	'CRAIOVA':          [['DOBRETA', 120], ['PITESTI', 138], ['RIMNICU VILCEA', 146]],
	'DOBRETA':          [['MEHADIA', 75], ['CRAIOVA', 120]],
	'EFORIE':           [['HIRSOVA', 86]],
	'FAGARAS':          [['SIBIU', 99], ['BUCHAREST', 211]],
	'GIURGIU':          [['BUCHAREST', 90]],
	'HIRSOVA':          [['EFORIE', 86], ['URZICENI', 98]],
	'IASI':             [['NEAMT', 87], ['VASLUI', 92]],
	'LUGOJ':            [['MEHADIA', 70], ['TIMISOARA', 111]],
	'MEHADIA':          [['LUGOJ', 70], ['DOBRETA', 75]],
	'NEAMT':            [['IASI', 87]],
	'ORADEA':           [['ZERIND', 71], ['SIBIU', 151]],
	'PITESTI':          [['RIMNICU VILCEA', 97], ['BUCHAREST', 101], ['CRAIOVA', 138]],
	'RIMNICU VILCEA':   [['SIBIU', 80], ['PITESTI', 97], ['CRAIOVA', 146]],
	'SIBIU':            [['RIMNICU VILCEA', 80], ['FAGARAS', 99], ['ARAD', 140], ['ORADEA', 151]],
	'TIMISOARA':        [['LUGOJ', 111], ['ARAD', 118]],
	'URZICENI':         [['BUCHAREST', 85], ['HIRSOVA', 98]],
	'VASLUI':           [['IASI', 92], ['URZICENI', 142]],
	'ZERIND':           [['ORADEA', 71], ['ARAD', 75]]
}
line_to_Bucharest={
    'ARAD':             418,
	'BUCHAREST':        0,
	'CRAIOVA':          239,
	'DOBRETA':          359,
	'EFORIE':           269,
	'FAGARAS':          211,
	'GIURGIU':          90,
	'HIRSOVA':          183,
	'IASI':             319,
	'LUGOJ':            504,
	'MEHADIA':          434,
	'NEAMT':            406,
	'ORADEA':           429,
	'PITESTI':          101,
	'RIMNICU VILCEA':   198,
	'SIBIU':            278,
	'TIMISOARA':        536,
	'URZICENI':         85,
	'VASLUI':           227,
	'ZERIND':           493
}

def BFS(city_paths:dict, start:str, goal:str) -> list:
	"""
    Accepts a start city and a goal city on city_paths and uses Binary First Search.
    Returns a list containing path of cities traveled through in search.
    """
	explored = []
	
	# Queue for traversing the
	# graph in the BFS
	queue = [[start]]
	
	# If the desired node is
	# reached
	if start == goal:
		return [start]
	
	# Loop to traverse the graph
	# with the help of the queue
	while queue:
		path = queue.pop(0)
		node = path[-1]
		
		# Condition to check if the
		# current node is not visited
		if node not in explored:
			neighbours = city_paths[node]
			
			# Loop to iterate over the
			# neighbours of the node
			for neighbour_node in neighbours:
				neighbour = neighbour_node[0]
				new_path = list(path)
				new_path.append(neighbour)
				queue.append(new_path)
				
				# Condition to check if the
				# neighbour node is the goal
				if neighbour == goal:
					#print("BFS Path = ", *new_path)
					return new_path
			explored.append(node)

	# Condition when the nodes
	# are not connected
	print("So sorry, but a connecting"\
				" path doesn't exist :(")
	return None

def DFS(city_paths:dict, start:str, goal:str) -> list:
    """
    Accepts a start city and a goal city on city_paths and uses Depth First Search.
    Returns a list containing path of cities traveled through in search.
    """
    explored = []

    # Stack for traversing the
    # graph in the DFS
    stack = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        return [start]

    # Loop to traverse the graph
    # with the help of the stack
    while stack:
        path = stack.pop()
        node = path[-1]
        
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = city_paths[node]
            
            # Loop to iterate over the
            # neighbours of the node
            for neighbour_node in neighbours:
                neighbour = neighbour_node[0]
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)
                
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    #print("DFS Path = ", *new_path)
                    return new_path
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
                " path doesn't exist :(")
    return None

def trip_distance(city_history:list) -> None:
    """
    Prints city-to-city travel distance as well as total distance traveled.
    """
    total=0
    itinerary=city_history
    for city in enumerate(itinerary):#city==(index,city name)
        if itinerary[city[0]]==itinerary[-1]:
            break
        for path in city_paths[city[1]]:
            if path[0] in itinerary[city[0]+1]:
                print(itinerary[city[0]],
                    "->", itinerary[city[0]+1],
                    "=",path[1],"km")
                total+=path[1]
    print("The total distance traveled will be",total,"km.")
    return None
####################### CLASS ####################################
class Traverse:

    distance_traveled=0
    city_history=[]

    def __init__(self,city:str,root:bool) -> None:
        """
        Creates a Traverse object adding city to city_history.\n
        The root variable indicates whether object created is root node
        or object formed through aStar recursion.
        """
        self.distance_traveled=0
        self.city_history.append(city)
        if root:
            self.city_history.clear()
            self.city_history.append(city)
            self.distance_traveled=0
    
    def aStar(self) -> tuple:
        """
        Recursively calls itself after finding the lowest cost path
        at each city.\n
        Returns (distance_traveled, city_history).
        """
        if self.city_history[-1]==DESTINATION: return self;
        paths=[]
        costs=[]
        for i in range(len(city_paths[self.city_history[-1]])):
            if city_paths[self.city_history[-1]][i][0] not in self.city_history:    #checks that city in city_paths has not been visited
                paths.append(city_paths[self.city_history[-1]][i])
        for path in paths:#path=[city,distance]
            costs.append(self.calculate_cost(path))
        lowest_cost_path=paths[costs.index(min(costs))]
        nextCity=Traverse(lowest_cost_path[0],False)
        self.distance_traveled+=lowest_cost_path[1]
        return nextCity.aStar()

    def calculate_cost(self,path:list) -> int:
        """f(n)=g(n)+h(n)"""
        return (self.distance_traveled+path[1])+line_to_Bucharest[path[0]]
####################    PROGRAMS    #####################
def find_shortest_route() -> None:
    """
    Loops path-finding prompt.
    """
    while True:
        # city=''
        # algo=''
        print(
        """ 
        This app finds a route from a city to the city of Bucharest.
        The user provides starting city and routing algorithm as input.
        The output is the algorithm chosen, cities traveled through,
        individual distances traveled, and total distance traveled.
        """)
        print(*list(city_paths.keys()))
        city=input("Which city do you want to depart from? ").upper()
        while city not in list(city_paths.keys()):
            city=input("Incorrect. Please select a city from the list: " ).upper()
        print("\nA -> A* | B -> BFS | D -> DFS")
        algo=input("Which algorithm would you like to use? ").upper()
        while algo not in ['A','B','D']:
            algo=input("Incorrect. Please select an algorithm from the list: " ).upper()
        if algo == 'A':
            print("\nYou have chosen to travel from",city,
                "to",DESTINATION,"using the A* heuristic search.")
            traverser=Traverse(city,True)
            traverser.aStar()
            trip_distance(traverser.city_history)
        elif algo == 'B':
            print("\nYou have chosen to travel from",city,
                "to",DESTINATION,"using the Breadth First Search.")
            traverser=BFS(city_paths,city,DESTINATION)
            trip_distance(traverser)
        else:
            print("\nYou have chosen to travel from",city,
                "to",DESTINATION,"using the Depth First Search.")
            traverser=DFS(city_paths,city,DESTINATION)
            trip_distance(traverser)
        if input("Type anything to find another route or X to exit: ").upper() == 'X':
            break
    return 0

def game() -> None:
    #do tic-tac-toe
    return

while True:
    answer=input("Enter 'Path' to find a route to Bucharest, 'Game' to play Tic-Tac-Toe, or X to exit: ").upper()
    while answer not in ['PATH','GAME','X']:
            answer=input("Incorrect. Please select a program to run: " ).upper()
    if answer == 'PATH':
        find_shortest_route()
    elif answer == 'GAME':
        game()
    else:
        break
