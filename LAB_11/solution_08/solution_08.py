MAZE_FILE = "maze.txt"



def corridorFinder(row, column, list):
    corridors = set()
    positions = [[row - 1, column], 
                 [row, column - 1], [row, column], [row, column + 1], 
                 [row + 1, column]]
    if row == len(list) - 1:
        positions = positions[:-1]
        if column == len(list) - 1:
            positions = positions[:-1]
    for r, c in positions:
        if (r != row or c != column) and list[r][c] == " ":
            pos = [r, c]
            pos = tuple(pos)
            corridors.add(pos)

    return corridors

def main():
    try:
        with open(MAZE_FILE, "r") as mazeFile:
            coordinates = []
            for line in mazeFile:
                line = line.rstrip()
                for word in line:
                    coordinates.append(word) 
    except IOError as error:
        print(f"There has been an error such as: {error}")
    except IndexError:
        print("lol")
    mazeDictionary = {}
    maze = [coordinates[i * 9:i * 9 + 9] for i in range(9)]
    for r in range(len(maze)):
        for c in range(len(maze)):
            if maze[r][c] != "*":
                key = [r , c]
                key = tuple(key)
                mazeDictionary[key] = (corridorFinder(r, c, maze))
                
    for key, value in mazeDictionary.items():
        print(f"{key} : {value}")

    for key, value in mazeDictionary.items():
        mazeDictionary[key] = "?"
        
    for key, value in mazeDictionary.items():
        print(f"{key} : {value}")


if __name__ == "__main__":
    main()