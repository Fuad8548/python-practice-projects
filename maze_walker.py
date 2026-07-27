# this is a project of practising python lists, tuples, loops & dictionaries  ......................

maze = [
    [".", "W", "W", "W", "W"],
    [".", ".", "W", "W", "W"],
    ["W", ".", ".", "W", "W"],
    ["W", "T", "W", "W", "W"],
    ["W", ".", ".", ".", "W"],
    ["W", "W", "W", "T", "."],
    ["W", "W", "W", "W", "G"]
]

player_pos = (2, 1)
move_history = []
player_pos_history = []

delta_lookup = {
    "up": (-1, 0), 
    "down": (1, 0),
    "left": (0, -1), 
    "right": (0, 1)
}
opposite_dir = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}

treasure_lookup = {
    # dictionary keys must be immutable, that's why tuple
    (3, 1): ("Ruby", 20), 
    (5, 3): ("Gold Coin", 50)
}
treasures_collected = []

for i, row in enumerate(maze):
    print(f"Row: {i}", end = " ")
    for cell in row:
        print(cell, end = " ")
    print()
        
while True:
    direction = input("Which way: (up/down/left/right/undo <n>/quit/restart/history/report/replay):")

    # If the player want to exit the game
    if direction == "quit":
        print("Thanks for playing!")
        break

    # If the player want a fresh start
    if direction == "restart":
        move_history.clear()
        player_pos_history.clear()
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
            reverse_direction = opposite_dir[move] 
            reverse_delta = delta_lookup[reverse_direction] 
            # player_pos[0] & player_pos[1] are the current row and column respectively 
            # reverse_delta[0] & reverse_delta[1] are the row and column changes respectively
            player_pos = (player_pos[0] + reverse_delta[0], player_pos[1] + reverse_delta[1])
        print(f"Undid last {undo_move_counter} move(s); {len(move_history)} move(s) remaining. Now back at {player_pos}")
        continue

    # final report ===============================
    # filter: count how many times each direction was used 
    if direction == "report":
        move_counts = {}
        for dir_name in delta_lookup:
            move_counts[dir_name] = len(list(filter(lambda m, d = dir_name: m == d, move_history)))

        print("move counts ============") 
        for dir_name, count in move_counts.items():
            print(f"{dir_name.capitalize()}: {count}")                       
        
        first_move, *rest = move_history
        print(f"\n You started by moving {first_move}, followed by {len(rest)} more move(s)")

        # .zip(): pair each move with the position it led to ==============
        print("\nStep by step replay") 
        for step_num, (move, pos) in enumerate(zip(move_history, player_pos_history)):
            print(f"Step {step_num}: moved {move} => landed at {pos}")
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

    # Treasure lookup and collection ---------------------------
    if maze[new_row][new_col] == "T":
        treasure = treasure_lookup[(new_row, new_col)]
        treasures_collected.append(treasure)
        maze[new_row][new_col] = "."
        print(f"You found a {treasure[0]} worth {treasure[1]} points!")

    # updating player position and move history
    player_pos = (new_row, new_col)
    move_history.append(direction)
    player_pos_history.append(player_pos)
    print("Moved", direction, ": at", player_pos)

    # if player reach the destination
    if maze[new_row][new_col] == "G":
        print("Voila! you reached the goal!")
        # calculate total collected treasure points ======================= 
        # sort treasure points from highest to lowest; 
        # .sorted() used instead of .sort() to get an instance of treasure_collected, keeping original list untouched
        # lambda function unanimously called and returned automatically in one line
        sorted_treasures = sorted(treasures_collected, key = lambda t: t[1], reverse = True)
        print(sorted_treasures)

        for name, value in sorted_treasures:
            print(f"{name}: {value} points")

        # map function here pulls the values of treasures_collected(points) and then sums up 
        total_score = sum(map(lambda t: t[1], treasures_collected))
        print(f"Total score: {total_score}")

        move_history.clear()
        break 
       
        
# In Python, maze[-1] doesn't error out — it wraps around and grabs the last row instead.
# (index -1 means "last item" in Python indexing). 
# So maze[-1][new_col] would actually check the bottom row of our maze, not "outside the grid