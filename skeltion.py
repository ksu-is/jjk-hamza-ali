
# 
# 
# two broken lines is the crouch optiion  i want to make it so the crouch option puts you into a new room 


# and the specality rooms

# i need to fix the teleport option 
# need to fix the crouch options 
#need to fix the  ---- how spacing works and looks
# need to make it more puzzel like for the options understand the flow for the puzze 
#  dsd dwdwdd  d sds      sdds






def show_instructions():
    print ("""
           
Shibuya Incident Adventure

==============
Commands:
go [north/south/teleport/west],  exit
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
        print("--- your sense paths:", ", ".join(directions))

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
        "teleport": "Portal Home",
        "text":"cursed spirts are everywhere and Satoru Gojo has been seeled. \nyou can go [north] to the Station to Save Gojo \nor you can go [teleport] back home if your to scared"

    },
    "Station Entrance": {
        "text": "You stand at the Station Entrance and the pressure feels off.\nYou can go [north] deeper into the station toward the Underground Platform.\nYou can go [south] into the Flooded Tunnel.\nOr you can go [teleport] back home.",
        "north": "Underground Platform",
        "south": "Flooded Tunnel",
        "teleport": "Portal Home"

    },

    "Underground Platform": {
        "text": "You step onto a dark Underground Platform. The lights flicker and distant footsteps echo through the station.\nYou can go [north] into the Deep Tunnel.\nYou can go [south] toward the Flooded Tunnel.\nOr you can go [teleport] back home.",
        "north": "Deep Tunnel",
        "south": "Flooded Tunnel",
        "teleport": "Portal Home"
    },

    "Deep Tunnel": {
        "text": "You move deeper into the station tunnels. The walls shake and cursed energy grows heavier with every step.\nYou can go [west] into the Service Corridor.\nOr you can go [ teleport] back home.",
        "west": "Service Corridor",
        "teleport": "Portal Home"

    },

    "Service Corridor": {
        "text": "A narrow Service Corridor runs beside broken train lines. The silence here feels unnatural.\nYou can go [south] toward the Flooded Tunnel.\nOr you can go [teleport] back home.",
        "south": "Flooded Tunnel",
        "telport": "Portal Home"
    },

    "Flooded Tunnel": {
        "text": "You are thrown into a Flooded Tunnel beneath Shibuya. Water crashes around your legs as danger closes in.\nYou can go [west] toward the Escape Route.\nYou can go [south] toward the Hidden Shelter.\nBut first, you must crouch to survive.",
        "west": "Escape Route",
        "south": "Hidden Shelter",
        "requires_crouch": True
    },

    "Escape Route": {
        "text": "You crawl into a damaged Escape Route lit only by emergency lights.\nYou can go [west] to the Tokyo Street Exit.\nOr you can go [south] to the Hidden Shelter.",
        "west": "Tokyo Street Exit",
        "south": "Hidden Shelter"
    },

    "Hidden Shelter": {
        "text": "Behind a broken wall, you find a Hidden Shelter where survivors are staying completely silent.\nYou can [stay] with them and remain hidden.\nYou can [talk] and risk making noise.\nOr you can go [teleport] back home.",
        "teleport": "Portal Home",
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
        cmd = input("You feel sukan presents you must 'crouch': ").strip().lower()

        if cmd != "crouch":
            print("You hesitate and Sukuna slashes you. GAME OVER 💀")
            return False

        print("Sukuna joins the battlefield.")
        print("Your two choices are: lower_head or Run")
        ans = input("Sukan \n  Your head is a bit high: ").strip().lower()

        if ans == "lower_head":
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
    
    # -------------------------
    # EXIT GAME
    # -------------------------
    elif action == "exit":
        print("Thanks for playing!")
        break

    else:
        print("Invalid command.\n")

    # -------------------------
    # telporting home
    # -------------------------
    if current_room == "Portal Home":
        print("You feel somthing sinester in your living room as you enter ")
        print("A cursed spirt bits your head.")
        print("GAME OVER 💀")
        break