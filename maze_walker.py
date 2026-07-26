# ..................... this is a project of practising python list, tuple methods and loops ......................

maze = [
    [".", "W", "W", "W", "W"],
    [".", ".", ".", ".", "W"],
    ["W", ".", "W", ".", "W"],
    ["W", ".", ".", "G", "W"],
    ["W", "W", "W", "W", "W"]
]

player_pos = (0, 0)
move_history = []
delta_lookup = {
    "up": (-1, 0), 
    "down": (1, 0),
    "left": (0, -1), 
    "right": (0, 1)
}
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
    direction = input("Which way: (up/down/left/right/undo <n>/quit/restart/history):")

    # If the player want to exit the game
    if direction == "quit":
        print("Thanks for playing!")
        break

    # If the player want a fresh start
    if direction == "restart":
        move_history.clear()
        player_pos = (0, 0)
        print("Let's get started again!")
        print(maze)
        continue

    # View move history with step numbers -------------
    if direction == "history":
        if not move_history:
            print("No moves yet.")
            continue

        for step_num, move in enumerate(move_history):
            print(f"Step {step_num}: {move}")
        continue

    # if player undo one or more moves ---------------
    if direction.startswith("undo"):
        count_undo_move = direction.replace("undo", "").strip()

        if not count_undo_move.isdigit():
            print("Usage: undo <number>, e.g., 'undo 2'")
            continue 

        undo_move_counter = int(count_undo_move)

        if undo_move_counter > len(move_history):
            print("Not enough moves to undo.")
            continue

        # updating player position after undoing move ----------------------
        # Grab the moves being undone BEFORE deleting anything
        moves_to_undo = move_history[-undo_move_counter:]
        # Delete them from history in one shot
        del move_history[-undo_move_counter:]

        # reversed() flips the order of moves_to_undo, so we process the most recently 
        # made move first — because undoing must happen in reverse chronological order till the last move remaining
        for move in reversed(moves_to_undo):
            # build reverse_delta dictionary, then immediately grab the value 
            # at key exactly same as the value of reverse_direction
            # returns value of the 'opposite' dictionary
            reverse_direction = opposite[move] 
            reverse_delta = delta_lookup[reverse_direction] 
            # player_pos[0] & player_pos[1] are the current row and column respectively 
            # reverse_delta[0] & reverse_delta[1] are the row and column changes respectively
            player_pos = (player_pos[0] + reverse_delta[0], player_pos[1] + reverse_delta[1])

        print(f"Undid last {undo_move_counter} move(s); {len(move_history)} move(s) remaining. Now back at {player_pos}")
        continue

    # player movement entry
    if direction not in delta_lookup:
        print("Not a valid direction! Try again")
        continue

    # from delta_lookup dictionary defined globally, immediately grab the value 
    # at key exactly same as the value of player input direction
    delta = delta_lookup[direction]

    # determining player positions ----------------
    new_row = player_pos[0] + delta[0]
    new_col = player_pos[1] + delta[1]

    # checking either the player crosses the border or is hindered by the wall
    if new_row < 0 or new_row >= len(maze) or new_col < 0 or new_col >= len(maze[0]):
        print("Nay! Out of the border!")
        continue  

    # check if there is wall ------------------
    if maze[new_row][new_col] == "W":
        print("There is wall, try a different direction.")
        continue

    # updating player position and move history
    player_pos = (new_row, new_col)
    move_history.append(direction)
    print("Moved", direction, ": at", player_pos)

    # if player reach the destination
    if maze[new_row][new_col] == "G":
        print("Voila! you reached the goal!")
        move_history.clear()
        break 
    

# In Python, maze[-1] doesn't error out — it wraps around and grabs the last row instead.
# (index -1 means "last item" in Python indexing). 
# So maze[-1][new_col] would actually check the bottom row of our maze, not "outside the grid