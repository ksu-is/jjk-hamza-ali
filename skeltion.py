# Text Adventure Game

def show_instructions():
    print("""
Adventure Game
==============
Commands:
go [north/south/east/west], get [item], use [item], run, crouch, stay, exit
Note: 'stay' is a special action available in some rooms (e.g., Quiet Waterfall).
""")

def show_status():
    print("---------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)
    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])
    print("---------------------------")

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
        "east": "Cave",
        "text": "You wake up groggy in a dark forest. Primal grunts echo around you... something is chasing you."
    },
    "River": {
        "text": "You reach a rushing river. Zombies are closing in. A small boat is tied to a post. You must use it to escape!",
        "north": "Ocean",
        "east": "ATV Cave",
        "south": "Waterfall Drop"
    },
    "Cave": {
        "west": "Forest",
        "text": "You stumble into a dim cave. Gold glitters on the ground.",
        "item": "gold"
    },
    "Ocean": {
        "text": "You row into open water. The zombies cannot reach you here.",
        "north": "Deep Sea",
        "south": "Waterfall Drop",
        "east": "ATV Cave"
    },
    "Deep Sea": {
        "text": "You dive below the shimmering water. A glowing golden key rests on the ocean floor.",
        "item": "gold_key",
        "south": "Ocean",
        "east": "Sea East",
        "west": "Sea West"
    },
    "Sea East": {
        "text": "The water grows shallow near rocks and shadowy shapes move inland.",
        "east": "ATV Cave",
        "west": "Deep Sea"
    },
    "ATV Cave": {
        "text": "Inside sits an ATV with a golden key slot. You hear zombies shrieking outside the cave entrance."
    },
    "Sea West": {
        "text": "The current tugs you toward a deafening roar of water.",
        "south": "Waterfall Drop",
        "east": "Deep Sea"
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
       "requires crouch: True"
        "text": "You reach civilization. People pull you to safety. You made it! 🏆",
        "end": True
    }
}

# -------------------------
# STARTING CONDITIONS
# -------------------------
current_room = "Forest"
inventory = []
used_boat = False

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

# -------------------------
# GAME START
# -------------------------
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
                print("\nYou whisper to Joel and Ellie. They thank you for staying quiet.")
                continue

    # -------------------------
    # MOVEMENT
    # -------------------------
    if action == "go":
        if len(move) < 2:
            print("Go where?\n")
            continue

        direction = move[1]

        if current_room == "River" and not used_boat:
            print("You can't swim across! You must 'use boat'.\n")
            continue

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way.\n")

    # -------------------------
    # GET ITEM
    # -------------------------
    elif action == "get":
        if len(move) < 2:
            print("Get what?\n")
            continue
        item = move[1]
        if "item" in rooms[current_room] and rooms[current_room]["item"] == item:
            inventory.append(item)
            print(f"You picked up the {item}!\n")
            del rooms[current_room]["item"]
        else:
            print("You can't get that.\n")

    # -------------------------
    # USE ITEMS
    # -------------------------
    elif action == "use":
        if len(move) < 2:
            print("Use what?\n")
            continue
        item = move[1]

        if item == "boat" and current_room == "River":
            print("You leap into the boat just in time and row to safety!\n")
            used_boat = True
            current_room = "Ocean"

        elif item == "gold_key" and current_room == "ATV Cave":
            if "gold_key" in inventory:
                print("\nThe ATV roars to life! You blast through the horde and escape!")
                if "gold" in inventory:
                    print("You escape rich. YOU WIN! 🏆")
                else:
                    print("You survive the apocalypse. YOU WIN! 🏆")
                break
            else:
                print("You don't have the key!\n")
        else:
            print("You can't use that here.\n")

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
    if current_room == "ATV Cave" and "gold_key" not in inventory:
        print("\nZombies pile into the cave—without a key, the ATV is useless.")
        print("GAME OVER 💀")
        break