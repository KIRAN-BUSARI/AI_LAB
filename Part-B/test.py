heuristic_cost = {
    "Arad": {"Bucharest": 366},
    "Bucharest": {"Bucharest": 0},
    "Craiova": {"Bucharest": 160},
    "Dobreta": {"Bucharest": 242},
    "Eforie": {"Bucharest": 161},
    "Fagaras": {"Bucharest": 176},
    "Giurgiu": {"Bucharest": 77},
    "Hirsowa": {"Bucharest": 151},
    "Lasi": {"Bucharest": 226},
    "Lugoj": {"Bucharest": 244},
    "Mehadia": {"Bucharest": 241},
    "Neamt": {"Bucharest": 234},
    "Oradea": {"Bucharest": 380},
    "Pitesti": {"Bucharest": 100},
    "Rimnicu Vilcea": {"Bucharest": 193},
    "Sibiu": {"Bucharest": 253},
    "Timisoara": {"Bucharest": 329},
    "Urziceni": {"Bucharest": 80}
}

def estimate_heuristic_cost(node,goal):
    return heuristic_cost[node][goal]

def a_star(graph,start,goal):
    open_set = [(0,start)]
    