# ..................... this is a project of practising python list, tuple methods and loops ......................

maze = [
    ["W", "W", "W", "W", "W"],
    [".", ".", ".", ".", "W"],
    ["W", ".", "W", ".", "W"],
    ["W", ".", ".", "G", "W"],
    ["W", "W", "W", "W", "W"]
]

player_pos = (0, 0)
move_history = []
opposite = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}

for i, row in enumerate(maze):
    print(f"Row: {i}", end = " ")
    for cell in row:
        print(cell, end = " ")
    print()
        
while True:
    direction = input("Which way: (up/down/left/right/undo/quit):")

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
    elif direction == "undo":
        if not move_history:
            print("No moves to undo yet!")
            continue        
    else:
        print("Not a valid direction! Try again")
        continue

    # determining player positions
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

    last_move = move_history.pop()
    reverse_direction = opposite[last_move] # returns value of the 'opposite' dictionary
    reverse_delta = {
        "up": (-1, 0), 
        "down": (1, 0),
        "left": (0, -1), 
        "right": (0, 1)
    }[reverse_direction]
    print(reverse_delta)

    player_pos = (player_pos[0] + reverse_delta[0], player_pos[1] + reverse_delta[1])
    print("Undid", last_move, "- now back at", player_pos)
    continue
    
print("Full move history:", move_history)


    



# In Python, maze[-1] doesn't error out — it wraps around and grabs the last row instead.
# (index -1 means "last item" in Python indexing). 
# So maze[-1][new_col] would actually check the bottom row of our maze, not "outside the grid