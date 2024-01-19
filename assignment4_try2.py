import sys
room_dict = {
    "start": ["south","","","","goblins_lair",""],
    "goblins_lair": [("east", "south", "west"), "You have entered the lair of the goblins. There you find a fat and grotesquely hairy goblin.","", "death_room","corridor_1","treasure_room"],
    "death_room": [(""),("You enter the dark room. You find the abyss. In your terror, you fall and perish."),"","","",""],
    "treasure_room": [("east"),("Amazing, you find a chest full of gold! Unfortunately your hands are full so you cannot take it with you."),"","goblins_lair","",""],
    "corridor_1": [("east"),("You enter a dark corridor, the first of many perhaps."),"","corridor_2","",""],
    "corridor_2": [("east", "south"), ("You have a choice: to your east lies a gigantic set of doors, to your south is a smaller much more inviting door."),"","boss_room","blessed_room",""],
    "blessed_room": [("north"), ("You receive the blessings of the abyss, perhaps this will help you in your final moments."),"corridor_2","","",""],
    "boss_room": [(""), ("You enter the final room. Before you lies a sleeping dragon."), 0],
}
current_location = "start"
blessing = 0
def move(current_location):
        print("\nWhich way would you like to go? You can go North, South, East, or West depending on the room you are in.")
        print("\nYou are currently located in room: " + str(current_location))
        moving = input("\nYou can move: " + str(room_dict[current_location][0]) + "\n").lower()
        verify = room_dict[current_location][0]
        if moving in verify:
            if moving == "north":
                current_location = room_dict[current_location][2]
                narrative(current_location)
                options(current_location)
                
            elif moving == "east":
                current_location = room_dict[current_location][3]
                narrative(current_location)
                if current_location == "death_room":
                    sys.exit(0)                 
                fight(current_location)                        
                options(current_location)
                
            elif moving == "south":
                current_location = room_dict[current_location][4] 
                narrative(current_location)
                fight(current_location)
                if current_location == "blessed_room":
                    room_dict["boss_room"][2] = 1       
                options(current_location)
                 
               
            elif moving == "west":
                current_location = room_dict[current_location][5]
                narrative(current_location)                
                options(current_location)
                  
        else:
            print("You have entered incorrectly, please enter North, South, East, or West, respectively.")           
            
            

def narrative(current_location):
    print(f"\nYou have entered {current_location}")
    print(room_dict[current_location][1])

def fight(current_location):

    if current_location == "goblins_lair":
        print("The hefty goblin approaches. What would you like to do?")
        fight_choice = input("You can fight (f), run (r), or cry (c).").lower()
        if fight_choice == "f": 
            print("Well done, you have stood your ground and have slain the goblin.")
            print("Now what would you like to do?")
        elif fight_choice == "r":
            print("There is nowhere to run. You are killed.")
            sys.exit(0)
        elif fight_choice == "c":
            print("Well that was unhelpful. You are killed.")
            sys.exit(0)
    elif current_location == "boss_room":
        print("You approach the sleeping dragon. What would you like to do?")
        fight_choice = input("You can fight (f), run (r), or cry (c).").lower()
        if room_dict["boss_room"][2] == 0:
            print("The dragon awakens and obliterates you. Take the hint next time.") 
            sys.exit(0)
        elif fight_choice == "f":
            print("The dragon awakens but due to your blessing, after an arduous battle you arise victorious.")
            print("Well done, you have completed The Abyss.")
            sys.exit(0)
        elif fight_choice == "r":
            print("There is nowhere to run. You are killed.")
            sys.exit(0)
        elif fight_choice == "c":
            print("Well that was unhelpful. You are killed.")
            sys.exit(0)
    else:
        print("You have entered incorrectly.")

def options(current_location):
    loop = True
    while loop == True:
        choices = str(input("""
        What would you like to do?
        You have three choices: move (m), hint (h), or quit (q).       
        """).lower()) 
        if choices != "m" and choices != "h" and choices != "q":
            print("You have entered incorrectly.")
            continue
        
        elif choices == "m":
            move(current_location)    

        elif choices == "h":
            if current_location == "goblins_lair" or current_location == "corridor_2":
                print("Choosing the right path can sometimes prove to be fortuitous.")
            else: print("There are no hints for this room.")
            continue
        elif choices == "q":
            loop = False
            print("You have finished.")
            break
        break
        


    
options("start")