# i fixed the structuring and blocking for the text in the game
# fix some spacing when it gives you instructions to be scentered 
# now it should run 

# i also want it to be a bit more sinster and add back the cut sceen 



 
# making a new room after the cut scean to send the player to so it dosnt loop the same thign s
# now its looping have to find the problem 
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
        "teleport": "Portal Home"
    },

    "Flooded Tunnel": {
        "text": "-",
        "west": "Escape Route",
        "south": "Hidden Shelter",
        "requires_crouch": True
    },
    
    

    "Escape Route": {
        "text": "Seconds before Sukan laughs as he kicks you out of the Tunnel, above into the Escape Route two floors above where you were \nbleeding out you crawl knowing you can retreat \ngo [west] to the Tokyo Street Exit.\ngo [south] to the Hidden Shelter where Gojo might be located",
        "west": "Tokyo Street Exit",
        "south": "Hidden Shelter"
    },

    "Hidden Shelter": {
        "text": "Behind a broken wall, you find the box carriers the esscents of Satoru Gojo /nbut since he's Saturo Gojo he is bound and cannot be moved from his current location \nyou can [stay] and wait and see if he breaks out on his own \nor You can [talk] risking alerting cursed spirts trying to use cursed speach to break the barrier",
        "special_actions": ["stay", "talk"]
    },

    "Portal Home": {
        "text": " feels off"
           
         
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
        cmd = input("You feel sukan presents forgot about your sensed path you must now  'crouch': ").strip().lower()
        print(" \n\n---------------------------")

        if cmd != "crouch":
            print("You hesitate and Sukuna slashes you. GAME OVER 💀")
            return False

        print("Sukuna appears. You can hardly breathe \nhis overwhelmingly evil presence peers into your soul..")
        print("Sukan speaks menecingly\nYour head is a bit high")
        ans = input("Your can: lower_head or Run: ").strip().lower()

        if ans == "lower_head":
            ans2 = input("Sukan speaks \nWhat is 9 + 10? 19 or 21: ").strip()
            if ans2 == "21":
                print("You can go [west] toward the Escape Route.\nYou can go [south] toward the Hidden Shelter.\nBut first, you must crouch to survive.")
                rooms[current_room]["crouched"] = True
                return "Escape Route"
            else:
                print("Wrong answer. Sukuna slashes you. GAME OVER 💀")
                return False
        else:
            print("Sukuna hits you with a cleave 💀")
            break


# --------------------
# GAME START
# --------------------
show_instructions()

while True:
    show_status()
    print(rooms[current_room]["text"])
    show_room_prompt()


    if rooms[current_room].get("requires_crouch") and not rooms[current_room].get("crouched"):
       new_room = run_crouch_check()
       if new_room is None:
            break
       current_room = new_room
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
        if current_room == "Hidden Shelter":
            if action == "stay":
                print("---------------------------\nGojo pops out the cursed object now unbound go in shibuya and kill sukan  .")
                print("You pass out thinking you saved everyone and now can rest ")
                print("YOU WIN!\n")
                break
            else:
                print("A cursed spirt jumps up and kills you ")
                print("seconds later gojo then pops out ")
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