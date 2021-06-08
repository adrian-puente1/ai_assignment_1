from os import path

DESTINATION='Bucharest'
city_paths = {
    'Arad':             [['Zerind', 75], ['Timisoara', 118], ['Sibiu', 140]],
	'Bucharest':        [['Urziceni', 85], ['Giurgiu', 90], ['Pitesti', 101], ['Fagaras', 211]],
	'Craiova':          [['Dobreta', 120], ['Pitesti', 138], ['Rimnicu Vilcea', 146]],
	'Dobreta':          [['Mehadia', 75], ['Craiova', 120]],
	'Eforie':           [['Hirsova', 86]],
	'Fagaras':          [['Sibiu', 99], ['Bucharest', 211]],
	'Giurgiu':          [['Bucharest', 90]],
	'Hirsova':          [['Eforie', 86], ['Urziceni', 98]],
	'Iasi':             [['Neamt', 87], ['Vaslui', 92]],
	'Lugoj':            [['Mehadia', 70], ['Timisoara', 111]],
	'Mehadia':          [['Lugoj', 70], ['Dobreta', 75]],
	'Neamt':            [['Iasi', 87]],
	'Oradea':           [['Zerind', 71], ['Sibiu', 151]],
	'Pitesti':          [['Rimnicu Vilcea', 97], ['Bucharest', 101], ['Craiova', 138]],
	'Rimnicu Vilcea':   [['Sibiu', 80], ['Pitesti', 97], ['Craiova', 146]],
	'Sibiu':            [['Rimnicu Vilcea', 80], ['Fagaras', 99], ['Arad', 140], ['Oradea', 151]],
	'Timisoara':        [['Lugoj', 111], ['Arad', 118]],
	'Urziceni':         [['Bucharest', 85], ['Hirsova', 98]],
	'Vaslui':           [['Iasi', 92], ['Urziceni', 142]],
	'Zerind':           [['Oradea', 71], ['Arad', 75]]
}
line_to_Bucharest={
    'Arad':             418,
	'Bucharest':        0,
	'Craiova':          239,
	'Dobreta':          359,
	'Eforie':           269,
	'Fagaras':          211,
	'Giurgiu':          90,
	'Hirsova':          183,
	'Iasi':             319,
	'Lugoj':            504,
	'Mehadia':          434,
	'Neamt':            406,
	'Oradea':           429,
	'Pitesti':          101,
	'Rimnicu Vilcea':   198,
	'Sibiu':            278,
	'Timisoara':        536,
	'Urziceni':         85,
	'Vaslui':           227,
	'Zerind':           493
}

class Traverse:

    distance_traveled=0
    city_history=[]

    def __init__(self,city) -> None:
        self.city_history.append(city)
    
    #fix distance traveled
    def aStar(self) -> tuple:
        """
        Recursively calls itself after finding the lowest cost path
        at each city.\n
        Returns a Traverse object
        """
        if self.city_history[-1]==DESTINATION: return self;
        paths=[]
        costs=[]
        for i in range(len(city_paths[self.city_history[-1]])):
            if city_paths[self.city_history[-1]][i][0] not in self.city_history:    #checks that city in city_paths has not been visited
                paths.append(city_paths[self.city_history[-1]][i])
        if not paths: return self,False;
        for path in paths:#path=[city,distance]
            costs.append(self.calculate_cost(path))
        lowest_cost_path=paths[costs.index(min(costs))]
        nextCity=Traverse(lowest_cost_path[0])
        self.distance_traveled+=lowest_cost_path[1]
        print(self.distance_traveled)
        return nextCity.aStar()

    def calculate_cost(self,path) -> int:
        """f(n)=g(n)+h(n)"""
        return (self.distance_traveled+path[1])+line_to_Bucharest[path[0]]

def bfs():
    #@Meike
    return None

def dfs():
    #@Meike
    return None

def find_shortest_route(): #reorganize after commit with bfs and dfs
  print("Purpose of app here")
  print("Which city do you want to depart from?")
  #print list of cities, could be list of keys from city_paths
  #accept city input
  print("Which algorithm would you like to use?")
  #print algos
  #accept algo input
  #select algorithm function
  #path=algo[root_city,0,[]]
  #print algo + cities visited + distances + total distance
  #loop or quit
  return 0


#Test beyond this point
tester=Traverse('Arad')
tester.aStar()

#print(tester.distance_traveled)
print(tester.city_history)