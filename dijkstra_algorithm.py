from heapq import *

from collections import defaultdict

def dijkstra(points, starting_point, ending_point):
    ground = defaultdict(list)

    for begin, finish, load in points:
        ground[begin].append((load, finish))

    place, visited = [(0, starting_point, ())], set()

    while place:
        (cost, destination, path) = heappop(place)

        if destination not in visited:
            visited.add(destination)
            path = (destination, path)

            if destination == ending_point:
                return(cost, path)
            
            for price, next_place in ground.get(destination, ()):
                if next_place not in visited:
                    heappush(place, (cost+price, next_place, path))
        print(place)
    
    return float("details")

if __name__ == "__main__":

    points = [
        ("Nairobi", "Dodoma", 15),
        ("Nairobi", "Mogadishu", 13),
        ("Dodoma", "Kampala", 16),
        ("Dodoma", "Mogadishu", 17),
        ("Dodoma", "Kigali", 15),
        ("Kampala", "kigali", 13),
        ("Mogadishu", "kigali", 13),
        ("Mogadishu", "Lusaka", 6),
        ("Kigali", "Lusaka", 16),
        ("Kigali", "Harare", 17),
        ("Lusaka", "Harare", 19)
    ]

print("Dijkstra Algorithm")

print("Nairobi >> Harare: ")

print (dijkstra(points, "Nairobi", "Harare"))