from typing import List
from collections import deque

def shortest_path(maze:List[List[str]]) -> int:
    rows, columns = len(maze), len(maze[0])
    directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]

    queue = deque([(0,0,1)])
    visited = set([(0,0)])

    while queue:
        x,y, length = queue.popleft()

        if x == y == 0:
            length -= 1
    
        if x == rows -1 and y == columns - 1:
            return length
    
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
    
            if 0 <= nx < rows and 0 <= ny < columns and maze[nx][ny] == '0' and (nx, ny) not in visited:
                queue.append((nx, ny, length +1))
                visited.add((nx, ny))

    return -1

maze = [
    ["0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "0"],
    ["0", "0", "0", "1", "0"]
]

print(shortest_path(maze))
