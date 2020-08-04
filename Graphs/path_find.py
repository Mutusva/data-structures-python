
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

maze = [
    ["S", "1", "0", "0"],
    ["0", "1", "0", "E"],
    ["0", "1", "0", "1"],
    ["1", "1", "1", "1"],
    ["0", "0", "1", "0"],
]


def find_path(start):
    Ylength = len(maze)
    Xlength = len(maze[start.y])
    visited = {}
    path_exists(maze, Ylength, Xlength, start, visited)
    for key in visited:
        print(key)
    
def path_exists(maze, ylength, xlength, point, visited):
    key = str(point.x) + '-' + str(point.y)
    
    if key not in visited:
        if point.y >= ylength or point.x >= xlength or point.x < 0 or point.y < 0:
            return False 
    
        if maze[point.x][point.y] == "0":            
            return False
        
        visited[key] = point  
        
        if maze[point.x][point.y] == "E":
            return True
        if maze[point.x][point.y] == "1" or maze[point.x][point.y] == "S" :
            return path_exists(maze, ylength, xlength, Point(point.x - 1, point.y) , visited) or path_exists(maze, ylength, xlength, Point(point.x + 1, point.y), visited) or path_exists(maze, ylength, xlength, Point(point.x, point.y - 1), visited) or path_exists(maze, ylength, xlength, Point(point.x, point.y + 1), visited)
    return False
    

find_path(Point(0,0))      