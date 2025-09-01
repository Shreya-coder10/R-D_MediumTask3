from collections import deque

def read_maze(filename):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file if line.strip()]
    return maze

def find_position(maze, char):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == char:
                return (i, j)
    return None

def print_maze(maze, path=None):
    if path:
        for i, j in path:
            if maze[i][j] not in ['S', 'E']:
                maze[i][j] = '.'
    for row in maze:
        print(''.join(row))
    print()

def solve_maze(start, end, maze):
  
    rows, cols = len(maze), len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

    queue = deque([(start, [start])]) 
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

    return None 


if __name__ == '__main__':
    filename = r'src\maze.txt'  #Make sure to set the path correctly
    maze = read_maze(filename)
    start = find_position(maze, 'S')
    end = find_position(maze, 'E')

    print("Original Maze:")
    print_maze(maze)

    path = solve_maze(start, end, maze)

    if path:
        print("Solved Maze with path:")
        print_maze(maze, path)
    else:
        print("No path found.")
