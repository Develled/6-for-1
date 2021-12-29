# global variable - carried through rooms

extra_chats = []


def Lab_Room():
    # Rough draft of Lab Room Puzzle

    # Defining Lab Room Variables
    inv = []
    inv_tt_puzzle = []

    Lab_Search = ['kyler', 'athena', 'grayson', 'bench', 'cabinet', 'skeleton', 'chamber', 'door', 'sink', 'computers',
                  'inventory']
    Puzzle_Confirm = ['yes', 'no']
    puzzle_start = ['inventory', 'puzzle', 'riddle']
    tt_answer = ['v', 'at', 'i', 'ca', 'n']

    input("You were the last to step in the room, As the door closed behind you, you heard a 'click.'")
    input(
        "You turned back around and noticed there was no door handle on the door, you tried pushing but as you'd expected, it didn't budge.")
    input(""""I don't think we're getting out that way" you mumbled.""")
    input(
        "You turned around to see Athena and Kyler staring at something Kyler was holding, neither seemed to hear you.")
    input('"What is it?" you asked.')
    input('"Vanadium" Kyler responded without averting his gaze.')
    input("""'Well this just raises more questions than answers' you thought silently.""")
    input(
        '''"It's a transition metal, I've never actually seen it in person before" Kyler continued as he lifted a test tube towards you.''')
    input("""As you look closer you notice a small label with a V and the number 23 on it.""")
    input(
        """"V is the element symbol for Vanadium, I had to study the periodic table for my degree" He explained as he continued to study the silvery-grey metal.""")
    input('''"Hold onto this will you" He asked as he handed you the test tube I'm going to look around some more."''')
    input('''"Uhhhhm ... okay."''')

    input('\n**V - Vanadium added to inventory**\n')

    inv.append('V - Vanadium')
    inv_tt_puzzle.append('v')

    input("Everyone disperses to different areas of the Lab.")
    input("You hadn't been in a lab since High School, this place looked a little more high tech than you remembered.")
    input(
        "The entire room was adorned by flags of different countries hung around the walls, which seemed a little odd for a science lab.")
    input(
        "Below the flags, along the wall to your right, there were some cabinets filled with science equipment, much of which you'd never seen before.")
    input("To your left, there was a row of 4 computers with monitors straight out of the mid 90's.")
    input(
        "The far side of the room had a door painted yellow and white, there was no door handle but you can see a small compartment to the right of the door.")
    input(
        "Behind you was the door you came in, and next to it you noticed there was one of those skeletons that seem to be in every science room.")
    input(
        "Right in front of you were 2 large black lab benches, the desk space itself was empty but you could see cut-outs in the sides for storing items.")
    input("On the end of the lab bench there was a small sink and an eye wash station.")
    input("Past the lab bench was a large clear compartment that had a 'Vacuum Chamber' label on it.")
    input(
        "You noticed Kyler went to another desk situated at the front of the room, it didn't look like a lab bench, more of a desk you would see a teacher use.")
    input("Athena was looking in the compartments of one of the Lab Benches.")
    input("Grayson was standing alone in one of the corners of the room, he didn't seem to be searching much.")
    input("You decided you should help look around the room.")

    investigate_lab_room = ""
    while investigate_lab_room not in Lab_Search:
        investigate_lab_room = input(
            "\nWhat would you like to investigate?\nType 'bench', 'cabinet', 'chamber', 'computers' 'door', 'sink' or 'skeleton' to investigate different areas of the room\nOr type 'Athena', 'Grayson', or 'Kyler' to talk to the others\nIf you would like to view your items type 'inventory'\n").lower()

        if investigate_lab_room == 'inventory':
            print('\nYou are currently holding:')
            input('\n'.join(inv))
            investigate_lab_room = ""

        # Searching Bench

        elif investigate_lab_room == 'bench':
            input("\nYou walk over to the closer lab bench, the one Athena isn't searching.")

            if 'N - Nitrogen' not in inv:
                input("The bench itself is pretty normal, the top is covered in a layer of dust.")
                input("Along the edges you can see some wood chipping.")
                input("There are two large openings used to store items, you reach your hand in and feel around.")
                input("You move your hand around until it grazes over some glass.")
                input("You grab the item and pull it out. Another test tube, this one looks empty but is labelled with an 'N' and the number '7'.")
                input('''"Nitrogen?" You guess as you turn towards Kyler with the test tube extended.''')
                input("Kyler looks up from the desk to examine the seemingly empty test tube, he gives you a quick nod and goes back to looking at the desk.")
                input("\n**N - Nitrogen added to inventory**\n")
                inv.append('N - Nitrogen')
                inv_tt_puzzle.append('n')
                investigate_lab_room = ""

            else:
                input("You look around the bench and reach into the openings again, but can't seem to find anything more.")
                investigate_lab_room = ""

        # Searching Cabinet

        elif investigate_lab_room == 'cabinet':
            input("\nYou walk over the the cabinets.")

            if 'Ta - Tantalum' not in inv:
                input("The cabinets themselves are filled with some weird sciencey stuff you'd never seen before.")
                input("Moving some of the instruments around you eventually find a test tube sitting at the back of the cabinet.")
                input("Pulling it out reveals a blueish-grey metal, the label on this test tube reads 'Ta' with a number '73'.")
                input("You bring the test tube over to Kyler to confirm the contents.")
                input("""He looks at it for what must have been half a second before answering; "That's Tantalum" he informs you""")
                input('''"Typically used to make high grade science equipment, it's actually pretty valuable"''')
                input("\n**Ta - Tantalum added to inventory**\n")
                inv.append('Ta - Tantalum')
                inv_tt_puzzle.append('ta')
                investigate_lab_room = ""

            else:
                input("There's still a lot of science equipment in here, but nothing that looks like it could help.")
                investigate_lab_room = ""

        # Searching Vacuum Chamber

        elif investigate_lab_room == 'chamber':
            input("\nYou head over to the 'Vacuum Chamber' separating the two lab benches.")

            if 'At - Astatine' not in inv:
                input("The chamber itself looks kind of like a big sauce pot with a pressure gauge.")
                input("You remove the lid and reach your hand in to find another test tube.")
                input("This test tube has a weird black metal rock in it.")
                input("The label on this one reads 'At' with a number '85' next to it.")
                input("Having no idea what 'At' could stand for you bring it to Kyler.")
                input('''"This... my god. How is this possible?" Kyler seems awestruck by the element.''')
                input('''"What is it?" You urge.''')
                input('''"It's called Astatine" he replies, his eyes still affixed on the test tube.''')
                input('''"I just... it only lasts for a couple hours before it decays completely. The most stable isotope has a half life of just over 8 hours."''')
                input("'That sounds kinda neat' you think to yourself. Kyler seems really attached to this one.")
                input('''"Thanks Kyler." You say as you slowly pull the test tube from his hands, his eyes seem locked to the substance.''')
                input("\n**At - Astatine added to inventory**\n")
                inv.append('At - Astatine')
                inv_tt_puzzle.append('at')
                investigate_lab_room = ""

            else:
                input("You take the lid off again and feel all around inside, but there's nothing left here.")
                investigate_lab_room = ""

        # Searching Computers

        elif investigate_lab_room == 'computers':
            input("\nYou make your way over to the block of computers.")

            if 'comp_1' not in extra_chats:
                input("'The computers look older than everything else in this lab' you think to yourself.")
                input("After looking around for a few minutes you determine there's nothing significant here.")
                extra_chats.append('comp_1')
                investigate_lab_room = ""

            elif 'news' not in extra_chats:
                input('You decide to to look around a bit more.')
                input('You look all around the computers and the bench and nothing seems to be stuck here.')
                input("It's pretty clear there are no more test tubes here.")
                input("As you turn to walk away, one of the computers lights up.")
                input("All of the computers seemed ancient and broken, you'd never expected one of them to be working.")
                input("You turn to the screen and see a newspaper article, dated 2 years ago.")
                input("Most of the article is blacked out, but you read what you can.")
                input(
                    "'[redacted] Seven bodies [redacted] fire at [redacted] college. [redacted] identified as local [redacted].")
                input(
                    "Below the text there is a picture of what looks like a burned up lecture hall. The hall itself doesn't look familiar.")
                input('''"Guys come over here! Look at this!" You call to out to everyone''')
                input("As everyone starts heading over the screen fades to black.")
                input("You vigorously wiggle the mouse connected to the display as Athena and Kyler make it to you.")
                input('''"Did you find something?" Athena asks''')
                input(
                    '''"Yes! I mean, I saw something. There was an article on this computer. I think it was talking about a fire. I'm trying to get it back."''')
                input('''"I ... I don't really know how that helps us?" Athena starts''')
                input(
                    '''"Don't think you're getting anything off this computer" Kyler follows "It's not plugged into anything."''')
                input('''"But I saw it already, it's working" you insisted''')
                input(
                    '''"I mean, we've all been in here a while now. I don't know about everyone else, but my minds kind of fuzzy." Kyler continues''')
                input(
                    '''"You could be seeing things, who knows what happened to us before arriving" Kyler walks off back to his desk''')
                input('''"But.. I know what-" you stammer "Let me know if it comes back" Athena cuts you off.''')
                input(
                    "You turn and lock eyes with her, both of you nod to each other as she goes back to investigating.")
                input(
                    "'I know what I saw.' You think to yourself; '..right? I have to trust my senses.. I have to trust something'")
                input("The computer isn't responding anymore, you decide to look around the room some more.")
                extra_chats.append('news')
                investigate_lab_room = ""

            else:
                input("You try getting the monitor to turn back on, but nothing you try works.")
                input("'I know what I saw' you reassure yourself.")
                investigate_lab_room = ""

        # Searching Sink

        elif investigate_lab_room == 'sink':
            input("\nYou head to the end of the bench where the small sink is.")
            input(
                "Turning the tap does nothing, it doesn't seem to be hooked up. You press down on the eye-washer and it's also disconnected.")
            input("You look around for a bit but it's clear nothing is hidden here.")
            investigate_lab_room = ""

        # Searching Skeleboy

        elif investigate_lab_room == 'skeleton':
            input("\nYou turn and come face to face with your inner self, a skeleton.")

            if 'Ca - Calcium' not in inv:
                input(
                    "You always thought these skeletons being in science labs was just a trope in TV, movies and video games but here we are.")
                input(
                    "The skeleton looks almost brand new, which seems a little out of place in a lab a lot of older equipment.")
                input(
                    "You poke around the bony bro and find another test tube, this one hidden behind the Skeleton's ribs.")
                input(
                    "'Ca; 20' is printed on the label. You don't need Kyler to tell you this is calcium, the silvery-white metal being attached to a bone almost seems like a weird joke.")
                input("\n**Ca - Calcium added to inventory**\n")
                inv.append('Ca - Calcium')
                inv_tt_puzzle.append('ca')
                investigate_lab_room = ""

            else:
                input("You can't see anything else hidden here.")
                investigate_lab_room = ""

        # Chatting with ya gurl

        elif investigate_lab_room == 'athena':
            input("\nYou decide to go see what Athena is up to.")

            if 'I - Iodine' not in inv:
                input('''"How's the search going?"''')
                input('''"Got some iodine" she says, holding a test tube up to you; "We sometimes used this back at the station to treat wounds."''')
                input("She hands you the test tube, you can see it labelled with an 'I' and a '53'.")
                input('''"Right, I can't imagine your life as a firefighter, how did you get into a field like that?"''')
                input('''"It's pretty simple really," she starts "I grew up as the oldest of 8, my mom worked hard but dad left when we were still young."''')
                input('''"I took up the mantle of protecting my siblings, I was going to make sure nothing bad ever happened to them."''')
                input('''"When I grew older, protecting is the only life I knew. I tried to figure out a way I could use that to help the world, instead of just my family."''')
                input('''"As a firefighter, I realized I could help protect everyone, while still looking out for my siblings. It was an easy choice really."''')
                input('''As she finishes she looks up to you, steely-eyed, her voice quiets and her tone becomes more determined.''')
                input('''"That's why I know I'm getting out of here, to make sure they're okay. To protect them. And protect everyone."''')
                input("Her eyes start to gloss over and she turns away, she looks more tense than before.")
                input('''"We'll all make it out of here." You say to the back of her head, "I promise."''')
                input("She doesn't acknowledge your words, you decide to leave her for now and continue looking. You can't just stand around now, you've made a promise after all.")
                input("\n**I - Iodine added to inventory**\n")
                inv.append('I - Iodine')
                inv_tt_puzzle.append('i')
                investigate_lab_room = ""

            elif 'ath_myst' not in extra_chats:
                input('"Find anything else?" you ask')
                input('''"Isn't there somewhere else you could look?" she snaps''')
                input('''"I uh.. I'm sor"- you stammer''')
                input(
                    '''"No, I'm sorry" she cuts you off "I've just been feeling really uneasy, I shouldn't have taken it out on you"''')
                input('''"Hey no worries" you reply "I don't think anyone is exactly comfortable in this situation"''')
                input('''"It's not just that. I just feel like... I don't know, this place feels too familiar"''')
                input('''"The lab?" you ask''')
                input(
                    '''"No not just the lab, this whole... facility. I don't even know where we are I just feel like.. I have a history here you know?"''')
                input(
                    '''"I know it sounds stupid, but ever since I woke up here I've felt a strange kind of presence with me. And not in a good way." She continued''')
                input('''"Like someone is standing over my shoulder, looking at me disapprovingly."''')
                input('''"Well, have you been here before? Did something happen" you ask''')
                input(
                    '''"I can't remember. I mean, there's bits and pieces. Like back in the hallway, a part of me knows I ran those halls before. But after that it's just .. blank"''')
                input(
                    '''"Why was I here? Was it real? What was I doing... I just keep digging and digging and I can't find anything."''')
                input(
                    '''"It might be nothing... but I just can't get away from it. It's like, a part of me *needs* to remember. But I can't quite reach it"''')
                input(
                    '''"I know it's right in front of me, whatever it is. I just need to keep reaching. There's bits and pieces flashing around me I just need to put them in the right place."''')
                input(
                    '''She looks up at you "Sorry, I didn't mean to put all this on you. We all have enough to worry about."''')
                input(
                    '''"No it's really no problem." you reply "We're in this together, and who knows what could help us. If you ever need anything from me just say the word"''')
                input(
                    '''Athena nods as a faint smile dances across her face "Thanks." she says "I'll keep that in mind"''')
                input("You smile back and step away to continue your search")
                extra_chats.append('ath_myst')
                investigate_lab_room = ""

            else:
                input("She looks deep in thought, you should probably leave her alone for now.")
                investigate_lab_room = ""

        # Science guy chatter

        elif investigate_lab_room == 'kyler':
            input("\nYou go check on Kyler at the desk.")

            if 'Y - Yttrium' not in inv:
                input('''"Hey Kyler, manage to find anything?"''')
                input(''''"Yttrium" he says as he hands you a test tube with a 'Y' and a small '39' printed on it.''')
                input("As you take it you start to wonder why you're the one in charge of holding onto everything.")
                input("Kyler looks lost in thought, you decide to check in on him.")
                input('''"How are you holding up?"''')
                input('''"I'm... weirdly fine." he answers.''')
                input('''"I think I've just spent so much time of my life in labs that I just feel at home here" he continues.''')
                input('''"Like, with whatever is going on right now I feel like I should be panicking you know? Or worrying, or something."''')
                input('''"But instead it feels almost nice to be back in a place like this. It feels so familiar, so comfortable. It's weird."''')
                input('''"But it brings back a lot of memories, a lot of better times." he turns to you with a smile. "So I'm fine right now, thank you for checking in"''')
                input('''"Of course!" You reply cheerfully; "Glad to hear you're doing okay.''')
                input("\n**Y - Yttrium added to inventory**\n")
                inv.append('Y - Yttrium')
                inv_tt_puzzle.append('y')
                investigate_lab_room = ""

            else:
                input("He seems to be reminiscing, he'll probably want some time alone.")
                investigate_lab_room = ""

        # Talking to Grayson

        elif investigate_lab_room == 'grayson':

            if 'Na - Sodium' not in inv:
                input("\nYou slowly head over towards Grayson.")
                input("Something about this man just feels ... unsettling.")
                input('"Hey Grayson, did you manage to find anything?"')
                input("Without saying anything he hands you a small tube.")
                input(""""What's this?" You ask as you take the tube from him.""")
                input('"Sodium." he mutters.')
                input('"Hey thanks! Where did you find this?"')
                input("Grayson just shrugs and turns away from you.")
                input("'Alright well... that was kinda painful' you think to yourself.")
                input("\n**Na - Sodium added to inventory**\n")
                inv.append('Na - Sodium')
                inv_tt_puzzle.append('na')
                investigate_lab_room = ""

            elif 'det_myst' not in extra_chats:
                input("\nYou decide to see if you can get anything more out of Grayson.")
                input(
                    '''"Hey Grayson, I know this situation sucks for all of us, but if we stick together I think we can figure it out"''')
                input("Grayson looks up at you and scoffs;")
                input('''"You don't know anything about this situation" he says to you under his breath.''')
                input('''"What do you mean? Do you know something we don't?"''')
                input(
                    '''"It's just..." he starts as he looks up at you; "Never mind, forget it." He finishes as he turns and walks away from you.''')
                input("There's clearly something he's hiding from everyone...")
                extra_chats.append('det_myst')
                investigate_lab_room = ""

            else:
                input("\nYou're not getting anything more out of him just yet, but you should keep an eye on him.")
                investigate_lab_room = ""

        elif investigate_lab_room == 'door':
            input("\nYou walk to the back of the room to check out the door.")
            input("The door itself is ... odd.")
            input(
                "There's an Italian flag hanging right above the door frame, and the door itself is Yellow on the left side and white on the right side.")
            input("Printed on the white side of the door is two crossed keys topped with a crown.")
            input(
                "The door itself has no handle, you try and push the door to see if anything happens but it doesn't move.")
            input(
                "To the right of the door theres a small alcove, and inside the alcove there's spaces for 5 test tubes.")
            input("You also notice some writing above the alcove that reads:")
            input("'A home to few but a refuge to many, \nthe world's smallest country bestows blessings a plenty'")

            if 'V - Vanadium' in inv and 'At - Astatine' in inv and 'I - Iodine' in inv and 'Ca - Calcium' in inv and 'N - Nitrogen' in inv:

                door_confirm = ""
                while door_confirm not in Puzzle_Confirm:
                    door_confirm = input(
                        "\nWould you like to try the puzzle?\nOnce you start the puzzle you cannot return to the room, make sure you have everything you need\nType 'Yes' or 'No'\n").lower()

                    if door_confirm == 'yes':
                        input('\nYou step closer to the alcove')
                        input("You look at the test tubes you're holding and the five test tube holders")

                        def lab_puzzle():

                            door_puzzle_lab = ""
                            while door_puzzle_lab not in puzzle_start:
                                door_puzzle_lab = input(
                                    "\n*Type 'inventory' to view your test tubes, 'puzzle' to attempt the puzzle or 'riddle' to re-read the text.*\n").lower()

                                if door_puzzle_lab == 'inventory':
                                    print('\nYou are currently holding:')
                                    input('\n'.join(inv))
                                    door_puzzle_lab = ""

                                elif door_puzzle_lab == 'riddle':
                                    input('\nYou study the written text again')
                                    input(
                                        "'A home to few but a refuge to many, \nthe world's smallest country bestows blessings a plenty'")
                                    door_puzzle_lab = ""

                                    # Need to add Return to leave puzzle and return to room

                                elif door_puzzle_lab == 'puzzle':
                                    input("\nYou take out the test tubes and begin to place them in the holders")
                                    input("\nType the ELEMENT SYMBOL next to the corresponding HOLDER.\n")
                                    answer = []
                                    while answer != tt_answer:

                                        a, b, c, d, e = input("Holder 1:").lower(), input("Holder 2:").lower(), input(
                                            "Holder 3:").lower(), input("Holder 4:").lower(), input("Holder 5:").lower()
                                        answer = [a, b, c, d, e]
                                        if answer == tt_answer:
                                            input(
                                                "\n'Vatican' you read to yourself, at that moment you hear a 'Bzzzzz!' noise.")
                                            input(
                                                "Everyone around the room looks up at you just as the door swings open.")
                                            input(
                                                '''"Well done!" Kyler bellows as he runs towards the door. "I knew you could get us out of here."''')
                                            input(
                                                "You turn and notice Grayson has already left, Kyler follows him out of the room as you step forward to see what lies ahead.")
                                            input("As you're about to take a step someone grabs you from behind.")
                                            input('''"Help me keep an eye on him" Athena whispers to you.''')
                                            input(
                                                '''"Something about Grayson seems... off to me. It doesn't sit right" she continues.''')
                                            input("You lock eyes with her and give her a curt nod.")
                                            input(
                                                "Athena runs ahead to catch up to the others, leaving you alone in the lab.")
                                            input("'Athena isn't wrong' you think 'There's something about Grayson.'")
                                            input(
                                                "You follow the others out of the room, determined to make it out of here alive.")

                                        elif a in inv_tt_puzzle and b in inv_tt_puzzle and c in inv_tt_puzzle and d in inv_tt_puzzle and e in inv_tt_puzzle:
                                            input(
                                                "\nThe test tube holders are all filled but nothing seems to be happening.")
                                            input(
                                                "'Hmmmm, mustn't be right' you think to yourself as you recollect the test tubes.")
                                            return lab_puzzle()

                                        else:
                                            input("\nInvalid Entry.\n")
                                            return lab_puzzle()

                                else:
                                    input("\nInvalid Entry\n")
                                    door_puzzle_lab = ""

                        lab_puzzle()

                    elif door_confirm == 'no':
                        input("\nYou decide to step away from the door for now.")
                        investigate_lab_room = ""

                    else:
                        input("\nInvalid Entry\n")
                        door_confirm = ""

            else:
                input("You decide to look around a bit more and come back here later.")
                investigate_lab_room = ""

        else:
            input('\nInvalid Entry\n')
            investigate_lab_room = ""


Lab_Room()

input("\n\nTo Be Continued\n\n")
