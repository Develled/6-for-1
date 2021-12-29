def First_Room():


#defining of variables for Room 1


    Folder_1=("FOLDER 1:\n NAME: de Jong, Kyler\n AGE: 28 \n OCCUPATION: Math Professor \n BIO: This is where my Bio would go .. IF I HAD ONE\n")
    Folder_2=("FOLDER 2:\n NAME: Bland-Lasso, Catalina \n AGE: 30 \n OCCUPATION: Nurse \n BIO: This is where my Bio would go .. IF I HAD ONE\n")
    Folder_3=("FOLDER 3:\n NAME: Sacre, Dax \n AGE: 19 \n OCCUPATION: Carpentry Apprentice \n BIO: This is where my Bio would go .. IF I HAD ONE\n")
    Folder_4=("FOLDER 4:\n NAME: Moraitis, Athena \n AGE: 23 \n OCCUPATION: Firefighter \n BIO: This is where my Bio would go .. IF I HAD ONE\n")
    Folder_5=("FOLDER 5:\n NAME: Giménez, Jada \n AGE: 22 \n OCCUPATION: Bartender \n BIO: This is where my Bio would go .. IF I HAD ONE\n")
    Folder_6=("FOLDER 6:\n NAME: Brewer, Grayson \n AGE: 26 \n OCCUPATION: Journalist \n BIO: [redacted]\n")
    Room_1 = ["table", "bunks", "door"]
    Table = ["writing", "folders"]
    Note=("\n'only six there shall be, to open the doors and set ye free'\n'a seventh will rear it's ugly head, strike them down or wind up dead'\n")
    Names=["dax", "jada", "kyler", "athena", "grayson", "catalina"]
    Puzzle_1=["slots", "folders"]
    Folders=["all", "1", "2", "3", "4", "5", "6"]
    Slots=["continue", "skip"]

test 123
#Room 1 Investigation


    input("Your eyes slowly open, you feel the cold floor below and start to look around.")
    input("You're in a room you've never seen before, everything is white, the flourescent lights beem down on you.")
    input("You slowly lift yourself up and try to gather your thoughts.")
    input("Your head is ringing and you feel dizzy, you put your hand on a nearby table to steady yourself and try taking in the room around you.")
    input("The air is thick with the smell of antiseptic which is not doing anything to stifle your headache.")
    input("As you look around the room you realize it is mostly empty. \nAll the furniture that remains are a couple of metal bunk bed frames with the mattresses removed and the table you're still leaning on.")
    input("At the other end of the room is what looks like a door, but you can't see any door handle.")
    investigate_room_1=""
    while investigate_room_1 not in Room_1:
        investigate_room_1=input("\nWhat would you like to investigate? Type 'table', 'bunks' or 'door'\n").lower()
        
        if investigate_room_1 == "bunks":
            input("\nThe bunk beds look old and out of place, in fact they stick out like a sore thumb.\nThe room looks clean and fresh and the beds are covered in rust. \nYou find it hard to believe that they provided much comfort even with a mattress. \nYou spend a few minutes poking around and can't find anything that could help you.")
            investigate_room_1=""
        
        elif investigate_room_1 == "door":
            print("\nYou walk over to the door, there is no door handle and where the handle should be instead has a blank display screen.\nYou try clicking around on the screen but it stays off. You try to push the door open but it doesn't even budge.") 
            print("You stick your fingers under the gap in the bottom and see if you can pull it from there but that just leads to some sore fingers. ")
            print("As you stand up you notice that there are six small slots to the right of the door, each with a number from 1-6 and roman numerals printed on them.") 
            input("You poke around but can't find anything useful here")
            investigate_room_1=""
        
        elif investigate_room_1 == "table":
            input("\nThe table is bolted to the floor, on top of it you see 6 manila folder's each with a name scrawled on them. \nBeneath the folders you can see what looks like red letters printed on the table")
        
            investigate_table=""
            while investigate_table not in Table:
                investigate_table=input("\nWhat would you like to look at first? Type 'folders' or 'writing' to investigate further.\n").lower()
            
                if investigate_table == "writing":
                    input("\nYou move the folders to the side and see a message painted onto the top of the table in large red letters that reads:")
                    input(Note)
                    print("The text seems like gibberish but gives off an unsettling aura")
                    input("You decide to instead turn your attention to the folders")
                    input("\nA total of six folders lay before you, each with a single sheet of paper inside. You open the folders one by one and read the contents\n")
                
                    input(Folder_1)
                    input(Folder_2)
                    input(Folder_3)
                    input(Folder_4)
                    input(Folder_5)
                    input(Folder_6)
                    input("each reads like a small dossier on a person, but none of the names sound familiar.")
                    input("You collect all the folders and decide to hold onto them since they're the only meaningful thing you've found so far and step away from the table")
                
            
                elif investigate_table == "folders":
                    input("\nA total of six folders lay before you, each with a single sheet of paper inside. You open the folders one by one and read the contents\n")
                
                    input(Folder_1)
                    input(Folder_2)
                    input(Folder_3)
                    input(Folder_4)
                    input(Folder_5)
                    input(Folder_6)
                    input("each reads like a small dossier on a person, but none of the names sound familiar.")
                    input("You collect them all anyway and decide to hold onto them since they're the only meaningful thing you've found so far.")
                    input("With the folders off the table, you can clearly see a message written in large red letters on top of the table that reads:")
                    input(Note)
                    input("The message makes you feel uneasy even though you don't fully understand what it's saying")
                    input("You collect your folders and slowly step away from the table")
                
                
                else:
                    input("invalid entry")
            
        else:
            input("invalid entry")
        
        
#Door Puzzle


    investigate_room_1=""
    while investigate_room_1 not in Room_1:
        investigate_room_1=input("\nWhat would you like to investigate? Type 'table', 'bunks' or 'door'\n").lower()
    
        if investigate_room_1 == "bunks":
            input("\nThe bunk beds look old and out of place, in fact they stick out like a sore thumb.\nThe room looks clean and fresh and the beds are covered in rust. \nYou find it hard to believe that they provided much comfort even with a mattress. \nYou spend a few minutes poking around and can't find anything that could help you.")
            investigate_room_1=""

        elif investigate_room_1 == "table":
            input(Note)
            input("The message is all that's left on the table now, reading it makes the hair on your neck stand up")
            investigate_room_1=""
        
        elif investigate_room_1 == "door":
            input("\nYou walk over to the door, there is no door handle and where the handle should be instead has a blank display screen.\nYou try clicking around on the screen but it stays off. You try to push the door open but it doesn't even budge.")
            input("As you step back you notice that there are six small slots to the right of the door, each with a number from 1-6 and roman numerals printed on them.")
            input("The roman numerals go from III to VIII in order with the slots.\nSo slot 1 has III printed on it, slot 2 has IV all the way up to slot 6 and VIII.")
            input("You look at the folders in your hand and realize that the six folders would fit perfectly in the six slots, you decide to try placing one folder in each slot.")
            def Door():
                door_puzzle=""
                while door_puzzle not in Puzzle_1:
                    door_puzzle=input("\nIf you would like to review the folders type 'folders'\nIf you would like to start placing folders in the slots type 'slots'\n").lower()
        
                    if door_puzzle == "folders":
                        folder_review=""
                        while folder_review not in Folders:
                            folder_review=input("\nWhich folder would you like to review?\nType a number from 1 - 6 to review the corresponding folder, or 'all' to review all folders\nType 'return' to go back\n").lower()
                        
                            if folder_review == "all":
                                  input(Folder_1)
                                  input(Folder_2)
                                  input(Folder_3)
                                  input(Folder_4)
                                  input(Folder_5)
                                  input(Folder_6)
                                  folder_review=""
                              
                            elif folder_review == "1":
                                 input(Folder_1)
                                 folder_review=""
                            elif folder_review == "2":
                                 input(Folder_2)
                                 folder_review=""
                            elif folder_review == "3":
                                 input(Folder_3)
                                 folder_review=""
                            elif folder_review == "4":
                                 input(Folder_4)
                                 folder_review=""
                            elif folder_review == "5":
                                 input(Folder_5)
                                 folder_review=""
                            elif folder_review == "6":
                                 input(Folder_6)
                                 folder_review=""
                        
                            elif folder_review == "return":
                                return Door()
                        
                            else:
                                input("invalid entry")
                    
                
                
                    elif door_puzzle == "slots":
                        input("You step towards the six slots with the folders in your hand.")
                        def Slot():
                            slot_puzzle=""
                            while slot_puzzle not in Slots:
                                slot_puzzle=input("\nWhat would you like to do? Type 'continue' to attempt the puzzle or 'return' to go back.\nOr type 'skip' if you're not smart enough to solve the puzzle and want to take the easy way out\n").lower()
                                
                                if slot_puzzle == "return":
                                    return Door()
                                    
                                
                                elif slot_puzzle == "continue":
                                    input("\nType the persons FIRST NAME next to the corresponding SLOT NUMBER - ROMAN NUMERAL\n")
                                    answer=[]
                                    while answer != Names:
                                        a, b, c, d, e, f = input("Slot 1 - III: ").lower(), input("Slot 2 - IV: ").lower(), input("Slot 3 - V: ").lower(), input("Slot 4 - VI: ").lower(), input("Slot 5 - VII: ").lower(), input("Slot 6 - VIII: ").lower()
                                        answer=[a, b, c, d, e, f]
                                        if answer==Names:
                                            input("The display screen lights up green and you hear a satisfying 'ding' sound\nThe door slowly swings open to a bright, white hallway.")
                                            input("You walk into the hallway, eager to get away from this weird place.")
                    
                                        elif a in Names and b in Names and c in Names and d in Names and e in Names and f in Names:
                                            input("The display screen blinks red and you hear a shrill buzzer\n'Hmmm something wasn't right' you think to yourself")
                                            return Slot()
                                         
                                        else:
                                            input("\ninvalid entry\n")
                                            
                                elif slot_puzzle == "skip":
                                    input("\nOh ... Okay.")
                                    input("Honestly I expected better of you. Such a shame.\n")
                                    input("You miraculously realize the incredibly simple solution to the puzzle.")
                                    input("\n'Hmmmm, all of these first names are different lengths and line up perfectly with the Roman Numerals'\nYou come up with all by yourself without any outside help.\n")
                                    input("You carefully place each folder in it's corresponding slot.\n")
                                    input("Slot 1 - III: Dax\nSlot 2 - IV: Jada\nSlot 3 - V: Kyler\nSlot 4 - VI: Athena\nSlot 5 - VII: Grayson\nSlot 6 - VIII: Catalina\n")
                                    input("The display screen lights up green and you hear a satisfying 'ding' sound\nThe door slowly swings open to a bright, white hallway.")
                                    input("You walk into the hallway, eager to get away from this weird place.")
                                    
                                   
                                else:
                                    input("invalid entry")
                                
                        Slot()            
            Door()
        
        else:
            input("invalid entry")
First_Room()

        
input("\n\nTo Be Continued\n\n")
