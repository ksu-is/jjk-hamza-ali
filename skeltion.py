# i remmoved the boat secition to  / the logic for it so that it can be pushed through out 
# removing exsees rooms and making it more structurly sound better 
# changed how the rooms are set up and how the movement between works 
def show_instructions():
    print ("""
Adventure Game
==============
Commands:
go [north/south/east/west], run, crouch, exit
""" ) 

def show_status():
    print("---------------------------")
    print("You are in the", current_room)

def show_room_prompt():
    directions = []
    for d in ["north", "south", "east", "west"]:
        if d in rooms[current_room]:
            directions.append(d)
            
    if directions:
        print("You sense paths:", ", ".join(directions))

    specials = rooms[current_room].get("special_actions", [])
    if specials:
        print("You can also:", ", ".join(specials))
    print()

# -------------------------
# ROOM DEFINITIONS
# -------------------------
rooms = {
    "Forest": {
        "north": "River",
        "east": "ATV Cave",
        "text": "You wake up groggy in a dark forest. Primal grunts echo around you... something is chasing you."
    },
    "River": {
        "text": "You reach a rushing river. Zombies are closing in. A small boat is tied to a post. You must use it to escape!",
        "north": "Ocean",
        "east": "ATV Cave",
        "south": "Waterfall Drop"
    },
   
    "Ocean": {
        "text": "You row into open water. The zombies cannot reach you here.",
        "north": "Deep Sea",
        "south": "Waterfall Drop",
        "east": "ATV Cave"
    },
    "Deep Sea": {
        "text": "You dive below the shimmering water. A glowing golden key rests on the ocean floor.",
        "east": "ATV Cave",
        "west": "Sea West"
    },
    
    #die 
    "ATV Cave": {
        "text": "Inside sits an ATV with a golden key slot. You hear zombies shrieking outside the cave entrance."
    },
    "Sea West": {
        "text": "The current tugs you toward a deafening roar of water.",
        "south": "Waterfall Drop",
        "east": "ATV Cave"
    },

    
    "Waterfall Drop": {
        "text": "You crash into the pool at the base of the waterfall! Zombies are surrounding the rocks — you must move quietly!",
        "west": "Civilization Path",
        "south": "Quiet Waterfall",
        "requires_crouch": True
    },

    "Civilization Path": {
        "text": "You are on rocky ground after the fall. Smoke rises from a town to the west. The waterfall roars to the south.",
        "west": "Mountain Town",
        "south": "Quiet Waterfall"
    },

    "Quiet Waterfall": {
        "text": "Behind the waterfall you find a father and daughter — Joel and Ellie — hiding in silence.",
        "east": "Civilization Path",
        "special_actions": ["stay", "talk"]
    },

    "Mountain Town": {
        "text": "You reach civilization. People pull you to safety. You made it! 🏆",
        "end": True
    }
}

# -------------------------
# STARTING CONDITIONS
# -------------------------
current_room = "Forest"

# -------------------------
# CROUCH PUZZLE FUNCTION 
# -------------------------
def run_crouch_check():
    """
    Forces crouch + math check before the player can move.
    FIXED: Sets crouched flag BEFORE room redraw so directions don't vanish.
    """
    while True:
        cmd = input("You must crouch to proceed (type 'crouch'): ").strip().lower()

        if cmd != "crouch":
            print("You must crouch here to sneak past the zombies.")
            continue

        print("\nTo move silently, answer this:")
        ans = input("What is the square root of 64? ").strip()

        if ans == "8":
            print("\nYou crouch low and move without a sound...")
            rooms[current_room]["crouched"] = True   # ⭐ FIXED
            return True
        else:
            print("\nCRACK! You stepped on a branch.")
            print("Zombies swarm you. GAME OVER 💀")
            return False

# --------------------
# GAME START
# --------------------
show_instructions()

while True:
    show_status()
    print(rooms[current_room]["text"])
    show_room_prompt()


    if rooms[current_room].get("requires_crouch") and not rooms[current_room].get("crouched"):
        print("Zombies are too close — you must crouch to sneak through!")
        if not run_crouch_check():
            break
        continue

    #  END GAME WHEN REACHING MOUNTAIN TOWN
    if rooms[current_room].get("end"):
        print("YOU WIN! 🏆")
        break

    move = input("What do you want to do? ").lower().split()
    if not move:
        continue

    action = move[0]

    # -------------------------
    # SPECIAL ACTIONS
    # -------------------------
    if action in rooms[current_room].get("special_actions", []):
        if current_room == "Quiet Waterfall":
            if action == "stay":
                print("\nJoel nods approvingly. Ellie hands you a carved wooden trophy.")
                print("You earned the Joel & Ellie Trophy! 🏆")
                print("YOU WIN!\n")
                break
            elif action == "talk":
                print("A cursed spirt jumps up and kills you ")
                break     # -------------------------
    # MOVEMENT
    # -------------------------
    if action == "go":
        if len(move) < 2:
            print("Go where?\n")
            continue

        direction = move[1]
            

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way.\n")

    # -------------------------
    # removed item and boat 
    
    # -------------------------
    # MANUAL CROUCH
    # -------------------------
    
    elif action == "crouch":
        print("\nTo move quietly, answer this:")
        ans = input("Square root of 64? ").strip()
        if ans == "8":
            print("You crouch silently.\n")
            rooms[current_room]["crouched"] = True
        else:
            print("CRUNCH! Zombies hear you. GAME OVER 💀")
            break

    # -------------------------
    # RUN OPTION
    # -------------------------
    elif action == "run" and current_room == "Civilization Path":
        print("\nYou sprint but the zombies are faster. GAME OVER 💀")
        break
    
    # -------------------------
    # EXIT GAME
    # -------------------------
    elif action == "exit":
        print("Thanks for playing!")
        break

    else:
        print("Invalid command.\n")

    # -------------------------
    # ATV CAVE DEATH WITHOUT KEY
    # -------------------------
    if current_room == "ATV Cave":
        print("\nZombies pile into the cave—without a key, the ATV is useless.")
        print("GAME OVER 💀")
        break