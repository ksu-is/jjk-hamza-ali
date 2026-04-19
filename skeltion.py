# Changing the code and story line to matach up with the plot in shibuya incdent and fixed the starting room 
# trying to implemnet a system where player can telport home betray their friends but for doing that they die 



def show_instructions():
    print ("""
Shibuya Incident Adventure

==============
Commands:
go [north/south/east/west], run,  exit
""" ) 

def show_status():
    print("---------------------------")
    print("You are in the", current_room)

def show_room_prompt():
    directions = []
    for d in ["north", "south", "teleport", "west"]:
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
    "Shibuya Crossing": {
        "north": "Station Entrance",
        "teleport ": "Portal Home",
        "text": "You wake up in  Shibuya Crossing. Sirens blaring and  civilians screaming with a sweral of and cursed energy filing  the air hearing the unthinkable Gojo sator has been seeled. \n Head [north] so i can go to [north] to the station to find Save Gojo \n or i can [teleport] back home while pissing a way my honor my honer away "
    },
    "Station Entrance": {
        "text": "You reach the entrance of Shibuya Station. The pressure feels off. \n You think i can head north underground can [telport ]",
        "north": "Underground Platform",
        "teleport ": "Portal Home",
        "south": "Flooded Tunnel"
    },

    "Underground Platform": {
        "text": "You step onto a dark underground platform. The lights flicker above you, and distant footsteps echo through the station.",
        "north": "Deep Tunnel",
        "south": "Flooded Tunnel",
        "east": "Portal Home"
    },

    "Deep Tunnel": {
        "text": "You move deeper into the station tunnels. The walls shake, and cursed energy grows heavier with every step.",
        "east": "Portal Home",
        "west": "Service Corridor"
    },

    "Service Corridor": {
        "text": "A narrow service corridor runs beside broken train lines. The concrete is cracked, and the silence feels unnatural.",
        "south": "Flooded Tunnel",
        "east": "Portal Home"
    },

    "Flooded Tunnel": {
        "text": "You are thrown into a flooded tunnel beneath Shibuya. Water crashes around your legs as danger closes in.",
        "west": "Escape Route",
        "south": "Hidden Shelter",
        "requires_crouch": True
    },

    "Escape Route": {
        "text": "You crawl into a damaged escape route lit only by emergency lights. A way out may be close.",
        "west": "Tokyo Street Exit",
        "south": "Hidden Shelter"
    },

    "Hidden Shelter": {
        "text": "Behind a broken wall, you find a hidden shelter where survivors are staying completely silent.",
        "east": "Portal Home",
        "special_actions": ["stay", "talk"]
    },

    "Portal Home": {
         
        
         
    },

    "Tokyo Street Exit": {
        "text": "You break through the final barrier and escape onto the outer streets of Tokyo. You survived Shibuya. 🏆",
        "end": True
    }
    
}

        

# -------------------------
# STARTING CONDITIONS
# -------------------------
current_room = "Shibuya Crossing"

# -------------------------
# CROUCH PUZZLE FUNCTION 
# -------------------------
def run_crouch_check():
    while True:
        cmd = input("You must crouch. Type 'crouch': ").strip().lower()

        if cmd != "crouch":
            print("You hesitate and Sukuna slashes you. GAME OVER 💀")
            return False

        print("Sukuna joins the battlefield.")
        print("Your two choices are: Lower_Head or Run")
        ans = input("Sukan \n  Your head is a bit high: ").strip()

        if ans == "Lower_Head":
            ans2 = input("Sukan speaks \n What is 9 + 10? 19 or 21: ").strip()
            if ans2 == "21":
                print("You are pushed further into the waterfall.")
                rooms[current_room]["crouched"] = True
                return True
            else:
                print("Wrong answer. Sukuna slashes you. GAME OVER 💀")
                return False
        else:
            print("Sukuna hits you with a cleave 💀")
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
    if current_room == "Portal Home":
        print("You feel somthing sinester in your living room as you enter ")
        print("A cursed spirt bits your head.")
        print("GAME OVER 💀")
        break