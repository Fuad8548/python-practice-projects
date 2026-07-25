maze = [
    ["W", "W", "W", "W", "W"],
    [".", ".", ".", ".", "W"],
    ["W", ".", "W", ".", "W"],
    ["W", ".", ".", "G", "W"],
    ["W", "W", "W", "W", "W"]
]

player_pos = (0, 0)
move_history = []

for i, row in enumerate(maze):
    print(f"Row: {i}", end = " ")
    for cell in row:
        print(cell, end = " ")
    print()
        
while True:
    direction = input("Which way: (up/ down/ left/ right/ quit):")

    if direction == "quit":
        print("Thanks for playing!")
        break

    if direction == "up":
        delta = (-1, 0)
    elif direction == "down":
        delta = (1, 0)
    elif direction == "left":
        delta = (0, -1)
    elif direction == "right":
        delta = (0, 1)         
    else:
        print("Not a valid direction! Try again")
        continue

    new_row = player_pos[0] + delta[0]
    new_col = player_pos[1] + delta[1]

    if new_row < 0 or new_col >= len(row):
        print("Nay! Out of the border!")
        continue  
    elif maze[new_row][new_col] == "W":
        print("There is wall, try a different direction")
        continue

    player_pos = (new_row, new_col)
    move_history.append(direction)
    print("Player moved", direction, ": at", player_pos)
    
    if maze[new_row][new_col] == "G":
        print("Voila! you reached the goal!")
        break 
    
print("Full move history:", move_history)
    





# In Python, maze[-1] doesn't error out — it wraps around and grabs the last row instead.
# (index -1 means "last item" in Python indexing). 
# So maze[-1][new_col] would actually check the bottom row of our maze, not "outside the grid