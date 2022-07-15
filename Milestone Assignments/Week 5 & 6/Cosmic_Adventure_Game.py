
title = 'Adventure Game: A Clash With A Cosmic Entity'
print (f'{title}')
print ()

# --- Introduction ---

intro = 'You are walking home one day after a wonderful day out with your friends. It is a very clear and sunny day with birds whistling and trees blowing in a cool and gentle breeze. You take in the sights, sounds and smells wholeheartedly and enjoy your blissful stroll home to the max. Upon arriving home your sister calls out to you saying that you received a package with a letter attached. “I left it in your room”, she says. You head upstairs and enter your room and there on your study desk sits the letter and package. “Should I \033[31mOPEN IT NOW\033[0m or \033[31mOPEN IT LATER\033[0m?”, you think to yourself.'
print (intro)
print()
open_now_or_later = input ('OPEN IT NOW or OPEN IT LATER? ').upper()
print ()

# --- First Choice Scenarios, Consequences, etc ---

if open_now_or_later in ('OPEN IT NOW', 'OPEN NOW', 'NOW'):
    name_of_sister = input ('Enter the name of your Sister: ').capitalize()
    print()
    now = f'Since you have nothing better to do you decide to open the package and the letter. The words on the letter read: “You have been chosen”. Upon completion of reading the letter it ignites into a white flame which consumes the whole letter. Shocked and bewildered at this sight but also extremely curious, you proceed to open the package. Inside you find a small square box about the size of your palm. You pick up the box, carefully examine it and then proceed to open the box. Upon doing so a flash of white light bursts from the box and shoots up like a pillar. You jump back and cover your eyes and the box levitates in front of you. All of a sudden, the pillar of light bends & shoots towards you and pierces your chest. You soon feel a surge going through you and continues to do so until all the light leaves the box and enters you after which the box disintegrates the same way the letter did. You then collapse on your bed and pass out until the next morning. You wake up the next morning in a haze, unable to properly recollect the events after your outing with your friends. You proceed to wash up and get finished for the day. You head down to breakfast in a tired and groggy state. Meeting your sister downstairs who is washing the dishes after preparing breakfast, she asks you what happened yesterday. “I’m… not sure… “, you respond. “I just collapsed and when I woke up this morning and everything about yesterday is a blur… I remember going out with friends from the university but that’s it…” You hold the front of your head as you speak this to your sister. “I’d better get ready for school”, you utter. “See you later, \033[36m{name_of_sister}\033[0m."'
    print (now)
    print ()

# -- General Scenario --

    your_name = input ('Enter Your Name: ').capitalize()
    your_gender = input ('Enter Your Gender M/F: ').upper()
    print()

# -- Female Route --

    if your_gender == 'F':
        you = f'You leave for university and travel your usual route. On your way you see a \033[33mman\033[0m a little way off. He seems to be struggling with something. You proceed to give him a hand and you then walk together afterwards. He introduce himself as \033[33mHenry\033[0m. “Oh, it’s nice to meet you. My name is \033[33m{your_name}\033[0m.” “It’s very nice to meet you”, he replies. You chat casually with your new friend when all of a sudden you hear a strange sound. “What was that?!?” You inquire, quite bewildered. Just then a cosmic entity appears before you.\n\nAfter exchanging glances, you suddenly see its hand glow. It then holds up its hand and blasts you with a beam of bright light. You are sent soaring several meters backwards and skid several feet on the ground before coming to a stop. Miraculously you are unharmed. You look up and see the entity charge towards you. “What’s going on?! What’s happening?!?” You ask in panic. Suddenly, A small feint voice echoes: “\033[32mHOLD YOUR HANDS OUT\033[0m in front of you, \033[32mSTARE AT THE ENTITY\033[0m or \033[32mSTART RUNNING\033[0m. Choose one,” the voice prompts.'
        print (you)
        print ()
        
        hands_eyes_feet = input('HOLD HANDS OUT, STARE AT ENTITY or START RUNNING? ').upper()
        print()

        if hands_eyes_feet in ('HOLD HANDS OUT', 'HOLD OUT HANDS', 'HANDS'):
            hands = 'You decide to hold out your hands and suddenly your hands begin to glow. Almost instantly after doing so a powerful blast in the form a beam is discharged from both hands. The power beams hit the entity with great force, this time flinging him backwards and crashing it into the ground.'
            print (hands)

        elif hands_eyes_feet in ('STARE', 'STARE AT ENTITY', 'STARE AT THE ENTITY', 'STARE AT'):
            eyes = 'Since you’re pretty much already looking at it you simply keep looking at it. Upon doing so your vision suddenly changes and the world around you changes colour. The background colour turns to a bluish colour and everything else appears white. The only difference is the entity. Different parts of the entity have spots of light brighter than the already white colour present in this new vision. You focus on all those spots, 11 in total. 2 on each upper and lower limb, 1 on the chest and 1 on the head. Bursts of energy come from all the spots you focus on, in a sort of mini explosion that sends the entity rolling on the ground.'
            print (eyes)

        elif hands_eyes_feet in ('START RUNNING', 'RUN', 'RUNNING', 'START TO RUN'):
            feet = 'Not wasting a second, you quickly jump to your feet and start running. As you begin running your speed drastically increases and you move so fast the naked eye cannot sense your movement. You stop and realise how far you ran, then you run back. Realising that you now have super speed it doesn’t take you long to figure out how to use your newfound speed to stop the entity. You begin running around the entity at supersonic speed, generating a tornado, which begins hurling the entity through the air. You then send the entity flying out the top where it crash-lands on an island off the coast of where you are.'
            print (feet)

        else:
            other = 'You are confused at what is happening and are unsure if you should trust the voice prompts you have received. As the entity closes in on you, you shield yourself with your arm, close your eyes and tilt your head forward. Upon doing so, a white light bursts forth from you repelling the entity and stopping it in its tracks. You quickly jump to your feet.'
            print (other)
        print ()

#  -- Male Route --

    if your_gender == 'M':
        you = f'You leave for university and travel your usual route. On your way you see a \033[33mwoman\033[0m a little way off. She seems to be struggling with something. You proceed to give her a hand and you then walk together afterwards. She introduce herself as \033[33mAlisha\033[0m. “Oh, it’s nice to meet you. My name is \033[33m{your_name}\033[0m.” “It’s very nice to meet you”, she replies. You chat casually with your new friend when all of a sudden you hear a strange sound. “What was that?!?” You inquire, quite bewildered. Just then a cosmic entity appears before you.\n\nAfter exchanging glances, you suddenly see its hand glow. It then holds up its hand and blasts you with a beam of bright light. You are sent soaring several meters backwards and skid several feet on the ground before coming to a stop. Miraculously you are unharmed. You look up and see the entity charge towards you. “What’s going on?! What’s happening?!?” You ask in panic. Suddenly, A small feint voice echoes: “\033[32mHOLD YOUR HANDS OUT\033[0m in front of you, \033[32mSTARE AT THE ENTITY\033[0m or \033[32mSTART RUNNING\033[0m. Choose one,” the voice prompts.'
        print (you)
        print ()
        
        hands_eyes_feet = input('HOLD HANDS OUT, STARE AT ENTITY or START RUNNING? ').upper()
        print()

        if hands_eyes_feet in ('HOLD HANDS OUT', 'HOLD OUT HANDS', 'HANDS'):
            hands = 'You decide to hold out your hands and suddenly your hands begin to glow. Almost instantly after doing so a powerful blast in the form a beam is discharged from both hands. The power beams hit the entity with great force, this time flinging him backwards and crashing it into the ground.'
            print (hands)

        elif hands_eyes_feet in ('STARE', 'STARE AT ENTITY', 'STARE AT THE ENTITY', 'STARE AT'):
            eyes = 'Since you’re pretty much already looking at it you simply keep looking at it. Upon doing so your vision suddenly changes and the world around you changes colour. The background colour turns to a bluish colour and everything else appears white. The only difference is the entity. Different parts of the entity have spots of light brighter than the already white colour present in this new vision. You Focus on all those spots, 11 in total. 2 on each upper and lower limb, 1 on the chest and 1 on the head. Bursts of energy come from all the spots you focus on, in a sort of mini explosion that sends the entity rolling on the ground.'
            print (eyes)

        elif hands_eyes_feet in ('START RUNNING', 'RUN', 'RUNNING', 'START TO RUN'):
            feet = 'Not wasting a second, you quickly jump to your feet and start running. As you begin running your speed drastically increases and you move so fast the naked eye cannot see your movements. You stop and realise how far you ran, then you run back. Realising that you now have super speed it doesn’t take you long to figure out how to use your newfound speed to stop the entity. You begin running around the entity at supersonic speed, generating a tornado, which begins hurling the entity through the air. You then send the entity flying out the top where it crash-lands on an island off the coast of where you are.'
            print (feet)

        else:
            other = 'You are confused at what is happening and are unsure if you should trust the voice prompts you have received. As the entity closes in on you, you shield yourself with your arm, close your eyes and tilt your head forward. Upon doing so, a white light bursts forth from you repelling the entity and stopping it in its tracks. You quickly jump to your feet.'
            print (other)

    print ()
    end = ' Ending '
    print (f'{end:=^220} ')
    print()

# --- Ending ---

    ending = 'Besting the entity with your newfouund powers it yields to you in submission and says, "Now you are as I am. You have now become a cosmic entity. I surrender all my powers to you. Becoming a being of the cosmos; forsake your human shell and embrace your destiny as one who travels among the stars, one who is able to bend the fabric of the cosmos to their will, one who visits many galaxies and many universes and many worlds, becoming stronger and doing with his/her power as they choose and see fit." After saying these words you absorb the power of the cosmic entity and it disintegrates into nothing. Taking the words you have received to heart, you decide to become a hero, fighting crime, assisting those in need and using your power in any positive way you can, no matter where it may be needed. A wonderful journey of exploration through the omniverse begins as you set out on an adventure to do good and visit as many different universes and their worlds as you can, with your new friend cheering you on and serving as your eternal companion through this new and wonderful time in your life.\n\nAnd thus concludes your first encounter with a cosmic entity. You have yielded significant fruit from the decions you have made.'
    print (ending)
    print ()

# --- Second Choice Scenarios, Consequences, etc ---

elif open_now_or_later in ('OPEN IT LATER', 'OPEN LATER', 'LATER'):
    name_of_friend = input ('Enter the name of your friend: ').capitalize()
    friend_gender = input ('Input their gender (M/F): ').upper()
    print ()

    if friend_gender == 'M':
        friend = f'Deciding that you were tired from your day’s events you leave the package unopened and proceed to the shower to wash up. You then head downstairs, seat yourself at the dining room table and engage in a casual conversation with your sister. “How was your outing?”, she asks. “It was wonderful, thank you \033[34m{name_of_friend}\033[0m told me about his recent university trip he took in order to complete a big semester project for his major. It was quite intriguing”, you respond. You continue to chat until dinner time, have dinner and then go on a nice long stroll together. You and your sister live together alone. After a wonderful leisurely time together, you get ready for the next morning and hit the sack. The next morning you wake up very refreshed and rejuvenated. You head down to breakfast after getting dressed and ready for the day, completely forgetting about the package you received. After eating breakfast, you get ready to head out to your university.'
        print (friend)
        print ()

    if friend_gender == 'F':
        friend = f'Deciding that you were tired from your day’s events you leave the package unopened and proceed to the shower to wash up. You then head downstairs, seat yourself at the dining room table and engage in a casual conversation with your sister. “How was your outing?”, she asks. “It was wonderful, thank you. \033[34m{name_of_friend}\033[0m told me about her recent university trip she took in order to complete a big semester project for her major. It was quite intriguing”, you respond. You continue to chat until dinner time, have dinner and go on a nice long stroll together. You and your sister live together alone. After a wonderful leisurely time together, you get ready for the next morning and hit the sack. The next morning you wake up very refreshed and rejuvenated. You head down to breakfast after getting dressed and ready for the day, completely forgetting about the package you received. After eating breakfast, you get ready to head out to your university.'
        print (friend)
        print ()
        
 # -- General Scenario --

    your_name = input ('Enter Your Name: ').capitalize()
    your_gender = input ('Enter Your Gender M/F: ').upper()
    print()

# -- Female Route --

    if your_gender == 'F':
        you = (f'You leave for university and travel your usual route. On your way you see a \033[33mman\033[0m a little way off. He seems to be struggling with something. You proceed to give him a hand and you then walk together afterwards. He introduce himself as \033[33mHenry\033[0m. “Oh, it’s nice to meet you. My name is \033[33m{your_name}\033[0m.” “It’s very nice to meet you”, he replies. You chat casually with your new friend when all of a sudden you hear a strange sound. “What was that?!?” You inquire, quite bewildered. Just then a cosmic entity appears before you.\n\nPointing at you with its right index finger, the entity announces: “You’re mine, Chosen.” “Get behind me!” Henry says. The entity then moves towards you. “Run!”, you exclaim. You both start running away from the entity and it chases you down. As you run you pass the street on which your house is on. Do you decide to \033[32mRUN HOME\033[0m, or \033[32mKEEP RUNNING STRAIGHT\033[0m?')
        print (you)
        print ()
        
        home_or_straight = input ('RUN HOME or RUN STRAIGHT? ').upper()
        print ()

        if home_or_straight in ('RUN HOME', 'HOME'):
            home = '“This way!”, you yell as you approach your house’s street. You bolt up the street and when you reach your house you run inside and bolt the door. You run up to your room and spy on the entity. “It doesn’t seem to have seen us come this way”, you say with relief. Henry notices the package on your desk and asks you what it is. You inform him that you received it yesterday but haven’t opened it yet. You tell Henry that if he wants to, he can open it. He proceeds to do so, revealing a small box the size of his palm. Just then the entity shows up. Taking the box from Henry you open it up. A flash of white light erupts from the box illuminating and covering the whole neighbourhood. When the light recedes and subsides, the entity and everything around you completely destroyed. Only you remain. '
            print (home)

        elif home_or_straight in ('RUN STRAIGHT', 'STRAIGHT', 'KEEP RUNNING STRAIGHT'):
            straight = 'You both keep running in the direction you were originally running in. As you run the entity draws nearer and nearer. Eventually the entity catches up and snatches you up in its one hand. After gripping you tightly and looking at you for a while it says, “Perhaps you are not the chosen one after all.” It drops you and then leaves. Suddenly you faint and when you wake up there is destruction that surrounds you on all sides. Your friend and everything around you are gone and you are left to stare in horror as there is nothing in your immediate vicinity that remains in tact.'
            print (straight)

        else:
            other_way = '“Which way should we run?!”, you ask Henry. “This way!”, he says. He starts running down your house’s street but in the opposite direction your house is. “There!”, Henry shouts, and points to an abandoned building at the bottom of the street. “That building has an underground bunker we can hide in!”, they exclaim. Not wasting a second, you head in the direction of the building and lock yourself in the bunker. You both fall asleep after about an hour in the bunker. When you awake your friend is gone and when you look outside all you see is destruction around you, with you as and at the epicenter.'
            print (other_way)
        print ()
    
# -- Male Route --

    if your_gender == 'M':
        you = f'You leave for university and travel your usual route. On your way you see a \033[33mwoman\033[0m a little way off. She seems to be struggling with something. You proceed to give her a hand and you then walk together afterwards. She introduce herself as \033[33mAlisha\033[0m. “Oh, it’s nice to meet you. My name is \033[33m{your_name}\033[0m.” “It’s very nice to meet you”, she replies. You chat casually with your new friend when all of a sudden you hear a strange sound. “What was that?!?” You inquire, quite bewildered. Just then an entity appears before you.\n\nPointing at you with its right index finger, the entity announces: “You’re mine, Chosen.” “Get behind me!” You say to your friend. The entity then moves towards you. “Run!”, Alisha exclaims. You both start running away from the entity and it chases you down. As you run you pass the street on which your house is. Do you decide to \033[32mRUN HOME\033[0m, or \033[32mKEEP RUNNING STRAIGHT\033[0m?'
        print (you)
        print ()
        
        home_or_straight = input ('RUN HOME or RUN STRAIGHT ').upper()
        print ()

        if home_or_straight in ('RUN HOME', 'HOME'):
            home = '“This way!”, you yell as you approach your house’s street. You bolt up the street and when you reach your house you run inside and bolt the door. You run up to your room and spy on the entity. “It doesn’t seem to have seen us come this way”, you say with relief. Alisha notices the package on your desk and asks you what it is. You inform her that you received it yesterday but haven’t opened it yet. You tell Alisha that if she wants to, she can open it. She proceeds to do so, revealing a small box the size of their palm. Just then the entity shows up. Taking the box from Alisha you open it up. A flash of white light erupts from the box illuminating and covering the whole neighbourhood. When the light recedes and subsides, the entity and everything around you completely destroyed. Only you remain.'
            print (home)

        elif home_or_straight in ('RUN STRAIGHT', 'STRAIGHT', 'KEEP RUNNING STRAIGHT'):
            straight = 'You both keep running in the direction you were originally running in. As you run the entity draws nearer and nearer. Eventually the entity catches up and snatches you up in its one hand. After gripping you tightly and looking at you for a while it says, “Perhaps you are not the chosen one after all.” It drops you and then leaves. Suddenly you faint and when you wake up there is destruction that surrounds you on all sides. Your friend and everything around you are gone and you are left to stare in horror as there is nothing in your immediate vicinity that remains in tact.'
            print (straight)

        else:
            other_way = '“Which way should we run?!”, you ask Alisha. “This way!”, she says. She starts running down your house’s street but in the opposite direction your house is. “There!”, Alisha shouts, and points to an abandoned building at the bottom of the street. “That building has an underground bunker we can hide in!”, they exclaim. Not wasting a second, you head in the direction of the building and lock yourself in the bunker. You both fall asleep after about an hour in the bunker. When you awake your friend is gone and when you look outside all you see is destruction around you, with you as and at the epicenter.'
            print (other_way)

    print ()
    end = ' Ending '
    print (f'{end:=^220} ')
    print()
        
# --- Ending ---
     
    ending = 'Left to muse and marvel on the singularity of the horrific scene before you, you begin making your way through the ruined area of the city in which you live. After wandering around for hours seeing no signs of life you decide to head in the direction of your universtiy. Feeling dejected and guilty for the event that took place you hang your head and slowly pace towards the university. As you reach the university entrance you hear someone cry out to you> "Hey!", the voice yells. You recognise that voice and immediately your spirits begin to be lifted. It is the voice of your sister. You turn in the direction of the voice and see your sister running towards you, "I am so glad you are okay!", she exclaims, throwing her arms around you. You immediately hug her back. After a rather lengthy embrace your sister asks, "What happened to you?!?" You then commence to relay everything to her about the package, the entity and the loss of your new friend. "I am so sorry," she says, shedding a tear. You both then walk to where your former house stood. "What are we going to now, sis? The house and everything in it are gone." "Do not worry", your sister says. Thankfully we still have the spare house. We can live there for the time being", she says with a smile. "We will be able to buy another house when the time comes. All that matters right now is that we are together and that we are alright." "I agree. Let us go home, Sis." You both head to your spare home and live continually thankful that you both have each other in your lives and that no matter what life throws at you both as long as you have each other, that is all that matters. And your friend? Well, let us just say that they are quietly watching you from the shadows, with a vow to protect the special bond that you and your sister share.\n\nAnd thus concludes your encounter with a cosmic entity. You have yielded significant fruit from the decions you have made.'
    print (ending)
    print ()

# --- Third Choice Scenario, Consequences, etc ---

else:
    none = 'Uncertain about which choice to make now you decide to worry about it later and proceed downstairs to assist your sister with preparing dinner and getting the house you both live in clean and tidy. You then both sit down to dinner and once you have both eaten, cleaned up and washed up you decide on how to spend the evening together. “Shall we \033[32mPLAY A GAME\033[0m or \033[32mWATCH SOMETHING\033[0m?’, Your sister asks.'
    print (none)
    print ()

    play_or_watch = input('PLAY A GAME or WATCH SOMETHING? ').upper()
    print ()

    if play_or_watch in ( 'PLAY A GAME', 'PLAY', 'GAME'):
        name_of_game = input('Enter Name of Game: ').capitalize()
        print ()
        play = f'“Let’s play a game”, you respond. “What shall we play?", Asks your sister. How about \033[35m{name_of_game}\033[0m? “Sounds like fun!”, your sister exclaims. So, you get out the game and proceed to play. As you play you reminisce about past times together and how much you’ve grown. You beat your sister at the game you play and then you both retire for the night.'
        print (play)
        print ()

    elif play_or_watch in ('WATCH SOMETHING', 'WATCH'):
        snack = input('Enter Snack Here: ')
        watch = f'“How about we watch something?”, you suggest. “I know just what to watch!”, your sister excitedly exclaims. She hops on to your favourite streaming site and shows you an action movie about cosmic and spiritual beings doing battle. “How about we have some snacks while we watch?’, says your sister. “Good idea I feel like some \033[36m{snack}\033[0m.” “Okay, I’ll have that too”, responds your sister. You both then get settled and watch the movie. Once it concludes you clean up and head to bed.'
        print (watch)

    else:
        neither = '“Neither”, you utter. “Perhaps we should retire early for the night.” “Perhaps you’re right. We both have big days tomorrow”, says your sister. You both then retire early for the night. You follow your usual morning when you wake up.'
        print (neither)
    print ()

# -- General Scenario --

    your_name = input ('Enter Your Name: ').capitalize()
    your_gender = input ('Enter Your Gender M/F: ').upper()
    print ()

# -- Female Route --

    if your_gender == 'F':
        you = (f'You leave for university and travel your usual route. On your way you see a \033[33mman\033[0m a little way off. He seems to be struggling with something. You proceed to give him a hand and you then walk together afterwards. He introduce himself as \033[33mHenry\033[0m. “Oh, it’s nice to meet you. My name is \033[33m{your_name}\033[0m.” “It’s very nice to meet you”, he replies. You chat casually with your new friend when all of a sudden you hear a strange sound. “What was that?!?” You inquire, quite bewildered. Just then an entity appears before you.\n\nThe entity looks at you and then says, “You have something I want.” “What do you want?”, you ask with a rather trembling voice. “The Package”, the entity replies. Before leaving the house, you decided to bring your package with you. You have it tucked away in your backpack. You take it out of your bag. Do you GIVE HIM THE PACKAGE or OPEN THE PACKAGE?')
        print (you)
        print ()

        give_or_open = input ('GIVE HIM THE PACAKGE or OPEN THE PACKAGE? ').upper()
        print ()

        if give_or_open in ('GIVE IT TO HIM', 'GIVE HIM THE PACKAGE', 'GIVE', 'GIVE PACKAGE'):
            give = 'Here, take it.” You hand the entity the package. “Wise choice”, the entity states. “You may just have saved your race and your galaxy, human.” The entity takes the package and ascends into the sky. Relieved that everything is now over you and Henry walk to the university together.'
            print (give)

        elif give_or_open in ('OPEN PACKAGE', 'OPEN THE PACKAGE', 'OPEN'):
            open_up = 'You open the package which contains a small box “No!”, the entity shouts but before it can get to you, you open the box and a bright light bursts forth from the box. When it recedes you and Henry stand there with blank looks on your faces. "What happened?", you ask, clutching your head, trying to recollect the events of the past morning. however, try as you might, everything about the package and the entity are wiped from both the memories of you and Henry.'
            print (open_up)

        else:
            other_choice = '“She will never give this to you!”, Henry yells and jumps in front of you. “Insolent pest!” The entity bellows. It then holds out its hand and Henry begins to levitate. He then suddenly starts choking, like he is being strangled. “Let him Go!” you scream, but the entity ignores you. You then open the package and as you do, the entity immediately lets Henry go and begins to absorb the radiant energy being emitted from the small palm-sized box your friend holds, while Henry gasps for air on all fours on the ground. Having absorbed the power the entity bellows in laughter and then snaps its fingers as it smirks at you. A brilliant light appears and you find yourself standing on the sidewalk. Unsure what to make of it, you shrug it off and head on to the university, Henry accompanying you.'
            print (other_choice)
        print ()

# -- Male Route --

    if your_gender == 'M':
        you = (f'You leave for university and travel your usual route. On your way you see a \033[33mwoman\033[0m a little way off. She seems to be struggling with something. You proceed to give her a hand and you then walk together afterwards. She introduce herself as \033[33mAlisha\033[0m. “Oh, it’s nice to meet you. My name is \033[33m{your_name}\033[0m.” “It’s very nice to meet you”, she replies. You chat casually with your new friend when all of a sudden you hear a strange sound. “What was that?!?” You inquire, quite bewildered. Just then an entity appears before you.\n\nThe entity looks at you and then says, “You have something I want.” “What do you want?”, you ask with a rather trembling voice. “The Package”, the entity replies. Before leaving the house, you decided to bring your package with you. You have it tucked away in your backpack. You take it out of your bag. Do you \033[30mGIVE HIM THE PACKAGE\033[0m or \033[30mOPEN THE PACKAGE\033[0m?')
        print (you)
        print ()

        give_or_open = input ('GIVE HIM THE PACAKGE or OPEN THE PACKAGE? ').upper()
        print ()

        if give_or_open in ('GIVE IT TO HIM', 'GIVE HIM THE PACKAGE', 'GIVE', 'GIVE PACKAGE'):
            give = 'Here, take it.” You hand the entity the package. “Wise choice”, the entity states. “You may just have saved your race and your galaxy, human.” The entity takes the package and ascends into the sky. Relieved that everything is now over you and Alisha walk to the university together.'
            print (give)

        elif give_or_open in ('OPEN PACKAGE', 'OPEN THE PACKAGE', 'OPEN'):
            open_up = 'You open the package which contains a small box “No!”, the entity shouts but before it can get to you, you open the box and a bright light bursts forth from the box. When it recedes you and Alisha stand there with blank looks on your faces. "What happened?", you ask, clutching your head, trying to recollect the events of the past morning. however, try as you might, everything about the package and the entity are whiped from both the memories of you and Alisha.'
            print (open_up)

        else:
            other_choice = '“I’ll never give this to you!”, You yell and toss the package to Alisha. “Insolent pest!” The entity bellows. It then holds out its hand and you begin to levitate. You then suddenly start choking, like you’re being strangled. “Let him Go!” Alisha screams, but the entity ignores her. She then opens the package and as they do, the entity immediately lets you go and begins to absorb the radiant energy being emitted from the small palm-sized box your friend holds, while you gasp for air on all fours on the ground. Having absorbed the power the entity bellows in laughter and then snaps its fingers as it smirks at you. A brilliant light appears and you find yourself standing on the sidewalk. Unsure what to make of it, you shrug it off and head on to the university, Alisha accompanying you.'
            print (other_choice)

    print ()
    end = ' Ending '
    print (f'{end:=^240}')
    print()
        
# --- Ending ---

    ending = 'Unaware of what could have been, you resume your regular daily life as a student and a sibling, with a new friend. It turns out that your new friend had just transferred to your university and happens to be taking your major as well. You thus spend a lot of time together with your sister and you 3 meet and visit often. Nothing about the entity or the package remains in the memory of you or your friend. You live out the rest of the days as a successful individual with wealth, providence and prestige. You go on to earn your doctorate in your designated major and become one of the most famous and renouned specialists in your respective field. You leave an unmatched legacy and an unconquerable empire in your wake and you use your power and influence to do all the good you can in the world you live in. Congratulations. It cannot get better than that, right? Or can it? ;)\n\nAnd thus concludes your encounter with a cosmic entity. You have yielded significant fruit from the decions you have made.'
    print (ending)
    print ()

conclusion = input ('Are you satisfied with the outcome (Yes/No)? ').capitalize()
print ()

if conclusion == 'Yes':
    satisfaction = True
else:
    satisfaction = False
if satisfaction:
    print ('Good fortune be upon you!\n\nTHANK YOU FOR PLAYING!!!')
if not satisfaction:
    print ('Why not give it another go until you find a result you like.\n\nTHANK YOU FOR PLAYING!!!')
print ()