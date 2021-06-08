from os import path

DESTINATION='Bucharest'

city_paths = {
    'Arad':             [['Zerind', 75], ['Timisoara', 118]],
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

def bfs(root_city,distance_traveled,city_history):
    city_history.append(root_city)
    if DESTINATION in city_history: #check all cities traveled to
        return (distance_traveled,city_history);
    paths=[]
    for i in range(len(city_paths[root_city])): #add all adjacent cities to paths
        paths.append(city_paths[root_city][i])
        if city_paths[root_city][i][0]==DESTINATION: #checks paths for Destination and returns Destination path if found
            return bfs(DESTINATION,distance_traveled+city_paths[root_city][i][1],city_history)
    
    
    return None

def a_star(root_city,distance_traveled,city_history):
    openList=[]
    closedList=[]
    
    return 0;

def find_shortest_route():
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
#find_shortest_route()
paths=[]
for i in range(len(city_paths['Arad'])):
    paths.append(city_paths['Arad'][i])
print(paths[0][0])